# SPDX-FileCopyrightText: 2022 Ludwig Hülk <@Ludee> © Reiner Lemoine Institut
# SPDX-FileCopyrightText: 2022 Jonas Huber <jh-RLI> © Reiner Lemoine Institut
# SPDX-FileCopyrightText: oemetadata <https://github.com/OpenEnergyPlatform/oemetadata/>
# SPDX-License-Identifier: MIT


def test_oemetadata_template_should_load():
    try:
        pass
    except Warning:
        print("Cannot open OEMetadata Template (v1.5.1)!")


def test_oemetadata_schema_should_validate_oemetadata_template():
    from jsonschema import ValidationError, validate

    from metadata.v1.v151.schema import OEMETADATA_V151_SCHEMA
    from metadata.v1.v151.template import OEMETADATA_V151_TEMPLATE

    try:
        validate(OEMETADATA_V151_TEMPLATE, OEMETADATA_V151_SCHEMA)
        print("OEMetadata Template is valid OEMetadata Schema (v1.5.1).")
    except ValidationError as e:
        print("Cannot validate OEMetadata Template with Schema (v1.5.1)!", e)
