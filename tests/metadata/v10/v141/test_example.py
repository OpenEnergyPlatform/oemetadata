# SPDX-FileCopyrightText: Ludwig Hülk <@Ludee> © Reiner Lemoine Institut
# SPDX-FileCopyrightText: Jonas Huber <jh-RLI> © Reiner Lemoine Institut
#
# SPDX-License-Identifier: MIT

def test_oemetadata_example_should_load():
    try:
        from metadata.v10.v141.example import OEMETADATA_V141_EXAMPLE
    except Warning:
        print("Cannot open OEMetadata Example (v1.4.1)!")


def test_oemetadata_schema_should_validate_oemetadata_example():
    from jsonschema import validate, ValidationError
    from metadata.v10.v141.example import OEMETADATA_V141_EXAMPLE
    from metadata.v10.v141.schema import OEMETADATA_V141_SCHEMA

    try:
        validate(OEMETADATA_V141_EXAMPLE, OEMETADATA_V141_SCHEMA)
        print("OEMetadata Example is valid OEMetadata Schema (v1.4.1).")
    except ValidationError as e:
        print("Cannot validate OEMetadata Example with Schema (v1.4.1)!", e)
