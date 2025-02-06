# SPDX-FileCopyrightText: 2021 Ludwig Hülk <@Ludee> © Reiner Lemoine Institut
# SPDX-FileCopyrightText: 2021 Jonas Huber <jh-RLI> © Reiner Lemoine Institut
# SPDX-FileCopyrightText: oemetadata <https://github.com/OpenEnergyPlatform/oemetadata/>
# SPDX-License-Identifier: MIT


def test_oemetadata_template_should_load():
    try:
        pass
    except Warning:
        print("Cannot open OEMetadata Template (v1.5.0)!")


def test_oemetadata_schema_should_validate_oemetadata_template():
    from jsonschema import ValidationError, validate

    from metadata.v1.v150.schema import OEMETADATA_V150_SCHEMA
    from metadata.v1.v150.template import OEMETADATA_V150_TEMPLATE

    try:
        validate(OEMETADATA_V150_TEMPLATE, OEMETADATA_V150_SCHEMA)
        print("OEMetadata Template is valid OEMetadata Schema (v1.5.0).")
    except ValidationError as e:
        print("Cannot validate OEMetadata Template with Schema (v1.5.0)!", e)
