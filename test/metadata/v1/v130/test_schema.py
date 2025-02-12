# SPDX-FileCopyrightText: 2019 Ludwig Hülk <@Ludee> © Reiner Lemoine Institut
# SPDX-FileCopyrightText: 2019 Jonas Huber <jh-RLI> © Reiner Lemoine Institut
# SPDX-FileCopyrightText: oemetadata <https://github.com/OpenEnergyPlatform/oemetadata/>
# SPDX-License-Identifier: MIT


def test_oemetadata_schema_should_load():
    try:
        pass
    except Warning:
        print("Cannot open OEMetadata Schema (v1.3.0)!")


def test_jsonschema_should_validate_oemetadata_schema():
    from jsonschema import ValidationError, validate

    from metadata.json_schema.draft07.schema import OEMETADATA_JSONSCHEMA_DRAFT07_SCHEMA
    from metadata.v1.v130.schema import OEMETADATA_V130_SCHEMA

    try:
        validate(OEMETADATA_V130_SCHEMA, OEMETADATA_JSONSCHEMA_DRAFT07_SCHEMA)
        print("OEMetadata Schema (v1.3.0) is valid JSON Schema.")
    except ValidationError as e:
        print("Cannot validate OEMetadata Schema with JSON Schema (v1.3.0)!", e)


def test_oemetadata_schema_should_have_correct_path():
    import string

    from metadata.v1.v130.schema import OEMETADATA_V130_SCHEMA

    def get_string(s):
        return string.printable + s + string.printable

    assert get_string(OEMETADATA_V130_SCHEMA["$schema"]) == get_string(
        "http://json-schema.org/draft-07/schema#"
    ), "Wrong schema path in OEMetadata Schema (v1.3.0)!"

    assert get_string(OEMETADATA_V130_SCHEMA["$id"]) == get_string(
        "https://raw.githubusercontent.com/OpenEnergyPlatform/oemetadata/production/metadata/v10/v130/schema.json"
    ), "Wrong id path in OEMetadata Schema (v1.3.0)!"
