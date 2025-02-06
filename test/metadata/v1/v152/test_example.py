# SPDX-FileCopyrightText: 2024 Ludwig Hülk <@Ludee> © Reiner Lemoine Institut
# SPDX-FileCopyrightText: 2024 Jonas Huber <jh-RLI> © Reiner Lemoine Institut
# SPDX-FileCopyrightText: oemetadata <https://github.com/OpenEnergyPlatform/oemetadata/>
# SPDX-License-Identifier: MIT


def test_oemetadata_example_should_load():
    try:
        pass
    except Warning:
        print("Cannot open OEMetadata Example (v1.5.2)!")


def test_oemetadata_schema_should_validate_oemetadata_example():
    from jsonschema import ValidationError, validate

    from metadata.v1.v152.example import OEMETADATA_V152_EXAMPLE
    from metadata.v1.v152.schema import OEMETADATA_V152_SCHEMA

    try:
        validate(OEMETADATA_V152_EXAMPLE, OEMETADATA_V152_SCHEMA)
        print("OEMetadata Example is valid OEMetadata Schema (v1.5.2).")
    except ValidationError as e:
        print("Cannot validate OEMetadata Example with Schema (v1.5.2)!", e)
