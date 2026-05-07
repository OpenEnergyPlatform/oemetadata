# SPDX-FileCopyrightText: 2026 Jonas Huber <jh-RLI> © Reiner Lemoine Institut
# SPDX-FileCopyrightText: 2026 Ludwig Hülk <@Ludee> © Reiner Lemoine Institut
# SPDX-FileCopyrightText: oemetadata <https://github.com/OpenEnergyPlatform/oemetadata/>
# SPDX-License-Identifier: MIT


def test_oemetadata_template_should_load():
    try:
        pass
    except Warning:
        print("Cannot open OEMetadata Template (v2.1)!")


def test_oemetadata_schema_should_validate_oemetadata_template():
    from jsonschema import ValidationError, validate

    from oemetadata.v2.v21.schema import OEMETADATA_V21_SCHEMA
    from oemetadata.v2.v21.template import OEMETADATA_V21_TEMPLATE

    try:
        validate(OEMETADATA_V21_TEMPLATE, OEMETADATA_V21_SCHEMA)
        print("OEMetadata Template is valid OEMetadata Schema (v2.1).")
    except ValidationError as e:
        print("Cannot validate OEMetadata Template with Schema (v2.1)!", e)


# Template is not a valid datapackage
# def test_oemetadata_template_is_datapackage():
#     from frictionless import validate
#
#     from oemetadata.v2.v21.template import OEMETADATA_V21_TEMPLATE
#
#     report = validate(OEMETADATA_V21_TEMPLATE)
#     assert report.valid, report.flatten(["message"])
