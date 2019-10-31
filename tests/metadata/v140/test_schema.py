import jsonschema


def test_if_schema_json_loads_successfully():
    from metadata.v140.schema import METADATA_V140_SCHEMA


def test_schema_against_example_which_should_succeed():
    from metadata.v140.schema import METADATA_V140_SCHEMA
    from metadata.v140.example import METADATA_V140_EXAMPLE

    assert jsonschema.validate(METADATA_V140_EXAMPLE, METADATA_V140_SCHEMA) == None
