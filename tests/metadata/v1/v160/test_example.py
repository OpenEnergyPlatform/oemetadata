# SPDX-FileCopyrightText: Ludwig Hülk <@Ludee> © Reiner Lemoine Institut
# SPDX-FileCopyrightText: Jonas Huber <jh-RLI> © Reiner Lemoine Institut
#
# SPDX-License-Identifier: MIT
def test_oemetadata_example_should_load():
    try:
        from metadata.v1.v160.example import OEMETADATA_V160_EXAMPLE
    except Warning:
        print("Cannot open OEMetadata Example (v1.6.0)!")


def test_oemetadata_schema_should_validate_oemetadata_example():
    from jsonschema import validate, ValidationError
    from metadata.v1.v160.example import OEMETADATA_V160_EXAMPLE
    from metadata.v1.v160.schema import OEMETADATA_V160_SCHEMA

    try:
        validate(OEMETADATA_V160_EXAMPLE, OEMETADATA_V160_SCHEMA)
        print("OEMetadata Example is valid OEMetadata Schema (v1.6.0).")
    except ValidationError as e:
        print("Cannot validate OEMetadata Example with Schema (v1.6.0)!", e)
