# SPDX-FileCopyrightText: 2024 Ludwig Hülk <@Ludee> © Reiner Lemoine Institut
# SPDX-FileCopyrightText: 2024 Jonas Huber <jh-RLI> © Reiner Lemoine Institut
#
# SPDX-License-Identifier: MIT

def test_oemetadata_schema_should_load():
    try:
        from metadata.latest.schema import OEMETADATA_LATEST_SCHEMA
    except Warning:
        print("Cannot open OEMetadata Schema (Latest)!")


def test_jsonschema_should_validate_oemetadata_schema():
    from jsonschema import validate, ValidationError
    from metadata.latest.schema import OEMETADATA_LATEST_SCHEMA
    from metadata.json_schema.draft2020_12.schema \
        import OEMETADATA_JSONSCHEMA_DRAFT202012_SCHEMA

    try:
        validate(OEMETADATA_LATEST_SCHEMA, OEMETADATA_JSONSCHEMA_DRAFT202012_SCHEMA)
        print("OEMetadata Schema (Latest) is valid JSON Schema (Draft 2020-12).")
    except ValidationError as e:
        print("Cannot validate OEMetadata Schema with JSON Schema (Latest)!", e)


def test_oemetadata_schema_should_have_correct_path():
    from metadata.latest.schema import OEMETADATA_LATEST_SCHEMA
    import string

    def get_string(s):
        return string.printable + s + string.printable

    assert get_string(OEMETADATA_LATEST_SCHEMA["$schema"]) == get_string(
        "https://json-schema.org/draft/2020-12/schema"
    ), "Wrong schema path in OEMetadata Schema (Latest)!"

    assert get_string(OEMETADATA_LATEST_SCHEMA["$id"]) == get_string(
        "https://raw.githubusercontent.com/OpenEnergyPlatform/oemetadata/production/metadata/latest/schema.json"
    ), "Wrong id path in OEMetadata Schema (Latest)!"
