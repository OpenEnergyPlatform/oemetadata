# SPDX-FileCopyrightText: 2024 Ludwig Hülk <@Ludee> © Reiner Lemoine Institut
# SPDX-FileCopyrightText: 2024 Jonas Huber <jh-RLI> © Reiner Lemoine Institut
# SPDX-FileCopyrightText: oemetadata <https://github.com/OpenEnergyPlatform/oemetadata/>
# SPDX-License-Identifier: MIT


def test_oemetadata_template_should_load():
    try:
        pass
    except Warning:
        print("Cannot open OEMetadata Template (Latest)!")


def test_oemetadata_schema_should_validate_oemetadata_template():
    from jsonschema import ValidationError, validate

    from metadata.latest.schema import OEMETADATA_LATEST_SCHEMA
    from metadata.latest.template import OEMETADATA_LATEST_TEMPLATE

    try:
        validate(OEMETADATA_LATEST_TEMPLATE, OEMETADATA_LATEST_SCHEMA)
        print("OEMetadata Template is valid OEMetadata Schema (Latest).")
    except ValidationError as e:
        print("Cannot validate OEMetadata Template with Schema (Latest)!", e)
