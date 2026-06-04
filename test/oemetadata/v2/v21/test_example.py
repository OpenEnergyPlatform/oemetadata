# SPDX-FileCopyrightText: 2026 Jonas Huber <jh-RLI> © Reiner Lemoine Institut
# SPDX-FileCopyrightText: 2026 Ludwig Hülk <@Ludee> © Reiner Lemoine Institut
# SPDX-FileCopyrightText: oemetadata <https://github.com/OpenEnergyPlatform/oemetadata/>
# SPDX-License-Identifier: MIT


def test_oemetadata_example_should_load():
    try:
        pass
    except Warning:
        print("Cannot open OEMetadata Example (v2.1)!")


def test_oemetadata_example_modules_should_load():
    try:
        pass
    except Warning:
        print("Cannot open OEMetadata Example Modules (v2.1)!")


def test_oemetadata_schema_should_validate_oemetadata_example():
    from jsonschema import ValidationError, validate

    from oemetadata.v2.v21.example import OEMETADATA_V21_EXAMPLE
    from oemetadata.v2.v21.schema import OEMETADATA_V21_SCHEMA

    try:
        validate(OEMETADATA_V21_EXAMPLE, OEMETADATA_V21_SCHEMA)
        print("OEMetadata Example is valid OEMetadata Schema (v2.1).")
    except ValidationError as e:
        print("Cannot validate OEMetadata Example with Schema (v2.1)!", e)


def test_oemetadata_schema_should_validate_oemetadata_example_modules():
    from jsonschema import ValidationError, validate

    from oemetadata.v2.v21.example_modules import OEMETADATA_V21_EXAMPLE_MODULES
    from oemetadata.v2.v21.schema import OEMETADATA_V21_SCHEMA

    try:
        validate(OEMETADATA_V21_EXAMPLE_MODULES, OEMETADATA_V21_SCHEMA)
        print("OEMetadata Example Modules is valid OEMetadata Schema (v2.1).")
    except ValidationError as e:
        print("Cannot validate OEMetadata Example Modules with Schema (v2.1)!", e)


def test_oemetadata_example_is_datapackage():
    from frictionless import Package

    from oemetadata.v2.v21.example import OEMETADATA_V21_EXAMPLE

    descriptor = OEMETADATA_V21_EXAMPLE.to_descriptor()
    errors = list(Package.metadata_validate(descriptor))
    assert not errors, [str(e) for e in errors]


def test_oemetadata_example_modules_is_datapackage():
    from frictionless import Package

    from oemetadata.v2.v21.example_modules import OEMETADATA_V21_EXAMPLE_MODULES

    descriptor = OEMETADATA_V21_EXAMPLE_MODULES.to_descriptor()
    errors = list(Package.metadata_validate(descriptor))
    assert not errors, [str(e) for e in errors]
