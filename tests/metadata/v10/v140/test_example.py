def test_if_example_json_loads_successfully():
    from metadata.v140.example import OEMETADATA_V140_EXAMPLE


def test_example_against_schema_which_should_succeed():
    import jsonschema
    from metadata.v140.example import OEMETADATA_V140_EXAMPLE
    from metadata.v140.schema import OEMETADATA_V140_SCHEMA

    assert jsonschema.validate(OEMETADATA_V140_EXAMPLE, OEMETADATA_V140_SCHEMA) == None
