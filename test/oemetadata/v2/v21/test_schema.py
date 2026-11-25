# SPDX-FileCopyrightText: 2026 Jonas Huber <jh-RLI> © Reiner Lemoine Institut
# SPDX-FileCopyrightText: 2026 Ludwig Hülk <@Ludee> © Reiner Lemoine Institut
# SPDX-FileCopyrightText: oemetadata <https://github.com/OpenEnergyPlatform/oemetadata/>
# SPDX-License-Identifier: MIT
import pytest


version_string = "OEMetadata-2.1.0"


@pytest.fixture
def schema():
    try:
        from oemetadata.v2.v21.schema import OEMETADATA_V21_SCHEMA as SCHEMA
        return SCHEMA
    except Exception as e:
        pytest.fail(f'Cannot open OEMetadata schema ({version_string})! {e}')


def test_oemetadata_schema_should_load(schema):
    pass


def test_jsonschema_should_validate_oemetadata_schema(schema):
    from jsonschema import ValidationError, validate

    from oemetadata.json_schema.draft2020_12.schema import (
        OEMETADATA_JSONSCHEMA_DRAFT202012_SCHEMA,
    )

    try:
        validate(schema, OEMETADATA_JSONSCHEMA_DRAFT202012_SCHEMA)
        print("OEMetadata Schema (v2.1) is valid JSON Schema (Draft 2020-12).")
    except ValidationError as e:
        pytest.fail(f"Cannot validate OEMetadata Schema with JSON Schema (v2.1)! {e}")


def test_oemetadata_schema_should_have_correct_path(schema):
    import string

    def get_string(s):
        return string.printable + s + string.printable

    assert get_string(schema["$schema"]) == get_string(
        "https://json-schema.org/draft/2020-12/schema"
    ), "Wrong schema path in OEMetadata Schema (v2.1)!"

    assert get_string(schema["$id"]) == get_string(
        "https://raw.githubusercontent.com/OpenEnergyPlatform/oemetadata/production/oemetadata/v2/v21/schema.json"
    ), "Wrong id path in OEMetadata Schema (v2.1)!"
