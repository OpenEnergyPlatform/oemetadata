# SPDX-FileCopyrightText: 2026 Jonas Huber <jh-RLI> © Reiner Lemoine Institut
# SPDX-FileCopyrightText: 2026 Ludwig Hülk <@Ludee> © Reiner Lemoine Institut
# SPDX-FileCopyrightText: oemetadata <https://github.com/OpenEnergyPlatform/oemetadata/>
# SPDX-License-Identifier: MIT
import pytest

from test.oemetadata.v2.v21.metadata_validation import ValidationError, validate_metadata


version_string = "OEMetadata-2.1.0"


@pytest.fixture
def template():
    try:
        from oemetadata.v2.v21.template import OEMETADATA_V21_TEMPLATE as TEMPLATE
        return TEMPLATE
    except Exception as e:
        pytest.fail(f'Cannot open OEMetadata template ({version_string})! {e}')


def test_oemetadata_template_should_load(template):
    pass


def test_oemetadata_schema_should_validate_oemetadata_template(template):
    try:
        validate_metadata(template, False, False, version_string)
        print(f"OEMetadata Template is valid OEMetadata Schema ({version_string}).")
    except ValidationError as e:
        pytest.fail(f"Cannot validate OEMetadata Template with Schema ({version_string})! {e}")


# Template is not a valid datapackage
# def test_oemetadata_template_is_datapackage(template):
#     try:
#         validate_metadata(template, False, True, version_string)
#         print(f"OEMetadata Template is a valid Frictionless DataPackage ({version_string}).")
#     except ValidationError as e:
#         pytest.fail(f"OEMetadata Template is not a valid Frictionless DataPackage ({version_string})! {e}")
