import functools
import importlib
import json
import re
import warnings

from frictionless import FrictionlessException, Package
import jsonschema


class ValidationError(Exception):
    """Exception raised when a validation fails."""


@functools.lru_cache
def split_version(version_string: str) -> tuple[str, str, str]:
    match = re.search(r'(\d+)\.(\d+)(\.\d+)?', version_string)
    if not match:
        raise ValueError('Passed invalid version string')
    patch_version = match.group(3)
    minor_version = match.group(2)
    major_version = match.group(1)
    if int(major_version) > 1:
        patch_version = ''
    return major_version, minor_version, patch_version


def get_metadata_version_module_path(version_string: str) -> str:
    major_version, minor_version, patch_version = split_version(version_string)
    return f'oemetadata.v{major_version}.v{major_version}{minor_version}{patch_version}'


# def get_metadata_version_module(version_string: str) -> ModuleType:
#     return importlib.import_module(get_metadata_version_module_path(version_string))


def get_metadata_schema(version_string: str) -> dict:
    normalized_version = ''.join(split_version(version_string))
    path = get_metadata_version_module_path(version_string)
    schema_module = importlib.import_module(f'{path}.schema')
    return getattr(schema_module, f'OEMETADATA_V{normalized_version}_SCHEMA')


def get_metadata_version(descriptor: dict) -> str:
    return descriptor["metaMetadata"]["metadataVersion"]


def validate_metadata(
        metadata: dict | str,
        check_license: bool = True,
        check_datapackage: bool = False,
        specific_version: str | None = None
) -> None:  # noqa: FBT001, FBT002
    """
    Validate metadata against related metadata schema.

    Parameters
    ----------
    metadata: dict | str
        Metadata as dict or as JSON string
    check_license: bool
        If set to True, licenses are validated
    check_datapackage: bool
        If set to True, attempts to load metadata as datapackage
    specific_version: str | None
        Validates against a specific schema version. If the data mismatches it is a validation error. A None value causes schema autodetection
    
    Returns
    -------
    None
        if metadata schema is valid. Otherwise it raises an exception.
    """
    if isinstance(metadata, str):
        metadata = parse_metadata(metadata)
    metadata_version = get_metadata_version(metadata)

    if specific_version is not None:
        if specific_version != metadata_version:
            raise ValidationError('Descriptor Metadata Version mismatch to expected version')

    metadata_schema = get_metadata_schema(metadata_version)
    try:
        jsonschema.validate(metadata, metadata_schema)
    except jsonschema.exceptions.ValidationError as ve:
        raise ValidationError(f"Error validating metadata against related metadata schema: {ve.message}") from ve
    if check_license:
        license.validate_oemetadata_licenses(metadata)
    __validate_optional_fields_in_metadata(metadata, metadata_schema)

    if check_datapackage:
        try:
            _ = Package.from_descriptor(metadata)
        except FrictionlessException as e:
            raise ValidationError("Loading Metadata as Datapackage failed") from e


def parse_metadata(metadata_string: str) -> dict:
    """
    Parse metadata string into a dictionary.

    Parameters
    ----------
    metadata_string: str
        Metadata given as JSOn string

    Returns
    -------
    dict
        Metadata as dictionary
    """

    def dict_raise_on_duplicates(ordered_pairs: dict) -> dict:
        """
        Reject duplicate keys.

        From https://stackoverflow.com/a/14902564/5804947
        """
        d = {}
        for k, v in ordered_pairs:
            if k in d:
                raise ValidationError(f"Duplicate keys in metadata: '{k}'")
            d[k] = v
        return d

    try:
        parsed_metadata = json.loads(metadata_string, object_pairs_hook=dict_raise_on_duplicates)
        return parsed_metadata  # noqa: TRY300
    except json.JSONDecodeError as jde:
        start = max(0, jde.pos - 10)
        end = min(len(metadata_string), jde.pos + 10)
        context = metadata_string[start:end]
        error_message = (
            f"Failed to decode JSON: "
            f"{jde.msg} at line {jde.lineno}, column {jde.colno}, position {jde.pos}. "
            f"Context around this position: '{context}'"
        )
        raise ValidationError(error_message) from jde


def __validate_optional_fields_in_metadata(metadata: dict, schema: dict) -> None:
    """
    Validate optional fields in metadata dictionary based on schema. Raise warnings if optional fields are missing.

    Parameters
    ----------
    metadata: dict
        Metadata as dictionary to check optional fields
    schema: dict
        JSONSchema for checking optional fields

    Returns
    -------
    None
    """

    def check_properties(sub_meta: dict, sub_schema: dict, current_path: str) -> None:
        """Check optional fields in metadata dictionary iteratively."""
        if "properties" not in sub_schema:
            return
        for field in sub_schema["properties"]:
            if ("required" not in sub_schema or field not in sub_schema["required"]) and field not in sub_meta:
                if current_path == "":
                    current_path = "top level"
                warnings.warn(f"Optional field '{field}' not found in metadata at {current_path}.", stacklevel=2)
            if field in sub_meta:
                new_path = field if current_path == "" else f"{current_path}.{field}"
                check_properties(sub_meta[field], sub_schema["properties"][field], new_path)

    check_properties(metadata, schema, "")
