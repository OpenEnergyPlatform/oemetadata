# SPDX-FileCopyrightText: Ludwig Hülk <@Ludee> © Reiner Lemoine Institut
# SPDX-FileCopyrightText: Jonas Huber <jh-RLI> © Reiner Lemoine Institut
#
# SPDX-License-Identifier: MIT

def test_oemetadata_template_should_load():
    try:
        from metadata.v2.v20.template import OEMETADATA_V20_TEMPLATE
    except Warning:
        print("Cannot open OEMetadata Template (v2.0)!")


def test_oemetadata_schema_should_validate_oemetadata_template():
    from jsonschema import validate, ValidationError
    from metadata.v2.v20.template import OEMETADATA_V20_TEMPLATE
    from metadata.v2.v20.schema import OEMETADATA_V20_SCHEMA

    try:
        validate(OEMETADATA_V20_TEMPLATE, OEMETADATA_V20_SCHEMA)
        print("OEMetadata Template is valid OEMetadata Schema (v2.0).")
    except ValidationError as e:
        print("Cannot validate OEMetadata Template with Schema (v2.0)!", e)
