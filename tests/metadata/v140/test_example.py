import jsonschema


def test_if_example_json_loads_successfully():
    from metadata.v140.example import METADATA_V140_EXAMPLE


def test_example_against_schema_which_should_succeed():
    from metadata.v140.example import METADATA_V140_EXAMPLE
    from metadata.v140.schema import METADATA_V140_SCHEMA

    assert jsonschema.validate(METADATA_V140_EXAMPLE, METADATA_V140_SCHEMA) == None
