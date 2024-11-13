# SPDX-FileCopyrightText: Ludwig Hülk <@Ludee> © Reiner Lemoine Institut
# SPDX-FileCopyrightText: Jonas Huber <jh-RLI> © Reiner Lemoine Institut
#
# SPDX-License-Identifier: MIT

def test_oemetadata_example_should_load():
    try:
        from metadata.v2.v20.example import OEMETADATA_V20_EXAMPLE
    except Warning:
        print("Cannot open OEMetadata Example (v2.0)!")


def test_oemetadata_schema_should_validate_oemetadata_example():
    from jsonschema import validate, ValidationError
    from metadata.v2.v20.example import OEMETADATA_V20_EXAMPLE
    from metadata.v2.v20.schema import OEMETADATA_V20_SCHEMA

    try:
        validate(OEMETADATA_V20_EXAMPLE, OEMETADATA_V20_SCHEMA)
        print("OEMetadata Example is valid OEMetadata Schema (v2.0).")
    except ValidationError as e:
        print("Cannot validate OEMetadata Example with Schema (v2.0)!", e)
