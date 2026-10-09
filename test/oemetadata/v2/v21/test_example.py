# SPDX-FileCopyrightText: 2026 Jonas Huber <jh-RLI> © Reiner Lemoine Institut
# SPDX-FileCopyrightText: 2026 Ludwig Hülk <@Ludee> © Reiner Lemoine Institut
# SPDX-FileCopyrightText: oemetadata <https://github.com/OpenEnergyPlatform/oemetadata/>
# SPDX-License-Identifier: MIT
import pytest
from test.oemetadata.v2.v21.metadata_validation import validate_metadata, ValidationError


version_string = "OEMetadata-2.1.0"


@pytest.fixture
def example():
    try:
        from oemetadata.v2.v21.example import OEMETADATA_V21_EXAMPLE as EXAMPLE
        return EXAMPLE
    except Exception as e:
        pytest.fail(f'Cannot open OEMetadata example ({version_string})! {e}')


@pytest.fixture
def example_modules():
    try:
        from oemetadata.v2.v21.example_modules import OEMETADATA_V21_EXAMPLE_MODULES as EXAMPLE_MODULES
        return EXAMPLE_MODULES
    except Exception as e:
        pytest.fail(f'Cannot open OEMetadata example with modules ({version_string})! {e}')


def test_oemetadata_example_should_load(example):
    pass


def test_oemetadata_example_modules_should_load(example_modules):
    pass


def test_oemetadata_schema_should_validate_oemetadata_example(example):
    try:
        validate_metadata(example, False, False, version_string)
        print(f"OEMetadata Example is valid OEMetadata Schema ({version_string}).")
    except ValidationError as e:
        pytest.fail(f"Cannot validate OEMetadata Example with Schema ({version_string})! {e}")


def test_oemetadata_schema_should_validate_oemetadata_example_modules(example_modules):
    try:
        validate_metadata(example_modules, False, False, version_string)
        print(f"OEMetadata Example Modules is valid OEMetadata Schema ({version_string}).")
    except ValidationError as e:
        pytest.fail(f"Cannot validate OEMetadata Example Modules with Schema ({version_string})! {e}")


def test_oemetadata_example_is_datapackage(example):
    try:
        validate_metadata(example, False, True, version_string)
        print(f"OEMetadata Example is a valid Frictionless DataPackage ({version_string}).")
    except ValidationError as e:
        pytest.fail(f"OEMetadata Example is not a valid Frictionless DataPackage ({version_string})! {e}")


def test_oemetadata_example_modules_is_datapackage(example_modules):
    try:
        validate_metadata(example_modules, False, True, version_string)
        print(f"OEMetadata Example with Modules is a valid Frictionless DataPackage ({version_string}).")
    except ValidationError as e:
        pytest.fail(f"OEMetadata Example with Modules is not a valid Frictionless DataPackage ({version_string})! {e}")
