# SPDX-FileCopyrightText: 2023 Ludwig Hülk <@Ludee> © Reiner Lemoine Institut
# SPDX-FileCopyrightText: 2023 Jonas Huber <jh-RLI> © Reiner Lemoine Institut
# SPDX-FileCopyrightText: oemetadata <https://github.com/OpenEnergyPlatform/oemetadata/>
# SPDX-License-Identifier: MIT


def test_oemetadata_schema_should_load():
    try:
        pass
    except Warning:
        print("Cannot open OEMetadata Schema (v1.6.0)!")


def test_jsonschema_should_validate_oemetadata_schema():
    from jsonschema import ValidationError, validate

    from oemetadata.json_schema.draft07.schema import (
        OEMETADATA_JSONSCHEMA_DRAFT07_SCHEMA,
    )
    from oemetadata.v1.v160.schema import OEMETADATA_V160_SCHEMA

    try:
        validate(OEMETADATA_V160_SCHEMA, OEMETADATA_JSONSCHEMA_DRAFT07_SCHEMA)
        print("OEMetadata Schema (v1.6.0) is valid JSON Schema.")
    except ValidationError as e:
        print("Cannot validate OEMetadata Schema with JSON Schema (v1.6.0)!", e)


def test_oemetadata_schema_should_have_correct_path():
    import string

    from oemetadata.v1.v160.schema import OEMETADATA_V160_SCHEMA

    def get_string(s):
        return string.printable + s + string.printable

    assert get_string(OEMETADATA_V160_SCHEMA["$schema"]) == get_string(
        "http://json-schema.org/draft-07/schema#"
    ), "Wrong schema path in OEMetadata Schema (v1.6.0)!"

    assert get_string(OEMETADATA_V160_SCHEMA["$id"]) == get_string(
        "https://raw.githubusercontent.com/OpenEnergyPlatform/oemetadata/production/oemetadata/v1/v160/schema.json"
    ), "Wrong id path in OEMetadata Schema (v1.6.0)!"
