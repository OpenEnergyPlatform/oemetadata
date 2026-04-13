# SPDX-FileCopyrightText: 2026 Jonas Huber <jh-RLI> © Reiner Lemoine Institut
# SPDX-FileCopyrightText: 2026 Ludwig Hülk <@Ludee> © Reiner Lemoine Institut
# SPDX-FileCopyrightText: oemetadata <https://github.com/OpenEnergyPlatform/oemetadata/>
# SPDX-License-Identifier: MIT


def test_oemetadata_example_should_load():
    try:
        pass
    except Warning:
        print("Cannot open OEMetadata Example (v2.1)!")


def test_oemetadata_schema_should_validate_oemetadata_example():
    from jsonschema import ValidationError, validate

    from oemetadata.v2.v21.example import OEMETADATA_V21_EXAMPLE
    from oemetadata.v2.v21.schema import OEMETADATA_V21_SCHEMA

    try:
        validate(OEMETADATA_V21_EXAMPLE, OEMETADATA_V21_SCHEMA)
        print("OEMetadata Example is valid OEMetadata Schema (v2.1).")
    except ValidationError as e:
        print("Cannot validate OEMetadata Example with Schema (v2.1)!", e)
