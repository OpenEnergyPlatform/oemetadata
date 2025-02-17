# SPDX-FileCopyrightText: 2024 Ludwig Hülk <@Ludee> © Reiner Lemoine Institut
# SPDX-FileCopyrightText: 2024 Jonas Huber <jh-RLI> © Reiner Lemoine Institut
# SPDX-FileCopyrightText: oemetadata <https://github.com/OpenEnergyPlatform/oemetadata/>
# SPDX-License-Identifier: MIT


def test_oemetadata_template_should_load():
    try:
        pass
    except Warning:
        print("Cannot open OEMetadata Template (v2.0)!")


def test_oemetadata_schema_should_validate_oemetadata_template():
    from jsonschema import ValidationError, validate

    from oemetadata.v2.v20.schema import OEMETADATA_V20_SCHEMA
    from oemetadata.v2.v20.template import OEMETADATA_V20_TEMPLATE

    try:
        validate(OEMETADATA_V20_TEMPLATE, OEMETADATA_V20_SCHEMA)
        print("OEMetadata Template is valid OEMetadata Schema (v2.0).")
    except ValidationError as e:
        print("Cannot validate OEMetadata Template with Schema (v2.0)!", e)
