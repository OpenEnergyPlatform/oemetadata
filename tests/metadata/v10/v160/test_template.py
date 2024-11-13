# SPDX-FileCopyrightText: Ludwig Hülk <@Ludee> © Reiner Lemoine Institut
# SPDX-FileCopyrightText: Jonas Huber <jh-RLI> © Reiner Lemoine Institut
#
# SPDX-License-Identifier: MIT
def test_oemetadata_template_should_load():
    try:
        from metadata.v10.v160.template import OEMETADATA_V160_TEMPLATE
    except Warning:
        print("Cannot open OEMetadata Template (v1.6.0)!")


def test_oemetadata_schema_should_validate_oemetadata_template():
    from jsonschema import validate, ValidationError
    from metadata.v10.v160.template import OEMETADATA_V160_TEMPLATE
    from metadata.v10.v160.schema import OEMETADATA_V160_SCHEMA

    try:
        validate(OEMETADATA_V160_TEMPLATE, OEMETADATA_V160_SCHEMA)
        print("OEMetadata Template is valid OEMetadata Schema (v1.6.0).")
    except ValidationError as e:
        print("Cannot validate OEMetadata Template with Schema (v1.6.0)!", e)
