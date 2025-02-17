# SPDX-FileCopyrightText: 2024 Ludwig Hülk <@Ludee> © Reiner Lemoine Institut
# SPDX-FileCopyrightText: 2024 Jonas Huber <jh-RLI> © Reiner Lemoine Institut
# SPDX-FileCopyrightText: oemetadata <https://github.com/OpenEnergyPlatform/oemetadata/>
# SPDX-License-Identifier: MIT


def test_oemetadata_template_should_load():
    try:
        pass
    except Warning:
        print("Cannot open OEMetadata Template (v1.5.2)!")


def test_oemetadata_schema_should_validate_oemetadata_template():
    from jsonschema import ValidationError, validate

    from oemetadata.v1.v152.schema import OEMETADATA_V152_SCHEMA
    from oemetadata.v1.v152.template import OEMETADATA_V152_TEMPLATE

    try:
        validate(OEMETADATA_V152_TEMPLATE, OEMETADATA_V152_SCHEMA)
        print("OEMetadata Template is valid OEMetadata Schema (v1.5.2).")
    except ValidationError as e:
        print("Cannot validate OEMetadata Template with Schema (v1.5.2)!", e)
