# SPDX-FileCopyrightText: 2022 Ludwig Hülk <@Ludee> © Reiner Lemoine Institut
# SPDX-FileCopyrightText: 2022 Jonas Huber <jh-RLI> © Reiner Lemoine Institut
# SPDX-FileCopyrightText: oemetadata <https://github.com/OpenEnergyPlatform/oemetadata/>
# SPDX-License-Identifier: MIT


def test_oemetadata_example_should_load():
    try:
        pass
    except Warning:
        print("Cannot open OEMetadata Example (v1.5.1)!")


def test_oemetadata_schema_should_validate_oemetadata_example():
    from jsonschema import ValidationError, validate

    from oemetadata.v1.v151.example import OEMETADATA_V151_EXAMPLE
    from oemetadata.v1.v151.schema import OEMETADATA_V151_SCHEMA

    try:
        validate(OEMETADATA_V151_EXAMPLE, OEMETADATA_V151_SCHEMA)
        print("OEMetadata Example is valid OEMetadata Schema (v1.5.1).")
    except ValidationError as e:
        print("Cannot validate OEMetadata Example with Schema (v1.5.1)!", e)
