# SPDX-FileCopyrightText: Ludwig Hülk <@Ludee> © Reiner Lemoine Institut
# SPDX-FileCopyrightText: Jonas Huber <jh-RLI> © Reiner Lemoine Institut
#
# SPDX-License-Identifier: MIT

def test_oemetadata_template_should_load():
    try:
        from metadata.v10.v151.template import OEMETADATA_V151_TEMPLATE
    except Warning:
        print("Cannot open OEMetadata Template (v1.5.1)!")


def test_oemetadata_schema_should_validate_oemetadata_template():
    from jsonschema import validate, ValidationError
    from metadata.v10.v151.template import OEMETADATA_V151_TEMPLATE
    from metadata.v10.v151.schema import OEMETADATA_V151_SCHEMA

    try:
        validate(OEMETADATA_V151_TEMPLATE, OEMETADATA_V151_SCHEMA)
        print("OEMetadata Template is valid OEMetadata Schema (v1.5.1).")
    except ValidationError as e:
        print("Cannot validate OEMetadata Template with Schema (v1.5.1)!", e)
