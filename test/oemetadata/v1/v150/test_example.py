# SPDX-FileCopyrightText: 2021 Ludwig Hülk <@Ludee> © Reiner Lemoine Institut
# SPDX-FileCopyrightText: 2021 Jonas Huber <jh-RLI> © Reiner Lemoine Institut
# SPDX-FileCopyrightText: oemetadata <https://github.com/OpenEnergyPlatform/oemetadata/>
# SPDX-License-Identifier: MIT


def test_oemetadata_example_should_load():
    try:
        pass
    except Warning:
        print("Cannot open OEMetadata Example (v1.5.0)!")


def test_oemetadata_schema_should_validate_oemetadata_example():
    from jsonschema import ValidationError, validate

    from oemetadata.v1.v150.example import OEMETADATA_V150_EXAMPLE
    from oemetadata.v1.v150.schema import OEMETADATA_V150_SCHEMA

    try:
        validate(OEMETADATA_V150_EXAMPLE, OEMETADATA_V150_SCHEMA)
        print("OEMetadata Example is valid OEMetadata Schema (v1.5.0).")
    except ValidationError as e:
        print("Cannot validate OEMetadata Example with Schema (v1.5.0)!", e)
