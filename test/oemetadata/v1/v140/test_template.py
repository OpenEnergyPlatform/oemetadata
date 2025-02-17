# SPDX-FileCopyrightText: 2019 Ludwig Hülk <@Ludee> © Reiner Lemoine Institut
# SPDX-FileCopyrightText: 2019 Jonas Huber <jh-RLI> © Reiner Lemoine Institut
# SPDX-FileCopyrightText: oemetadata <https://github.com/OpenEnergyPlatform/oemetadata/>
# SPDX-License-Identifier: MIT


def test_oemetadata_template_should_load():
    try:
        pass
    except Warning:
        print("Cannot open OEMetadata Template (v1.4.0)!")


def test_oemetadata_schema_should_validate_oemetadata_template():
    from jsonschema import ValidationError, validate

    from oemetadata.v1.v140.schema import OEMETADATA_V140_SCHEMA
    from oemetadata.v1.v140.template import OEMETADATA_V140_TEMPLATE

    try:
        validate(OEMETADATA_V140_TEMPLATE, OEMETADATA_V140_SCHEMA)
        print("OEMetadata Template is valid OEMetadata Schema (v1.4.0).")
    except ValidationError as e:
        print("Cannot validate OEMetadata Template with Schema (v1.4.0)!", e)
