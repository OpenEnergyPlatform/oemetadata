def test_if_example_json_loads_successfully():
    from metadata.v141.example import OEMETADATA_V141_EXAMPLE


def test_example_against_schema_which_should_succeed():
    import jsonschema
    from metadata.v141.example import OEMETADATA_V141_EXAMPLE
    from metadata.v141.schema import OEMETADATA_V141_SCHEMA

    assert jsonschema.validate(OEMETADATA_V141_EXAMPLE, OEMETADATA_V141_SCHEMA) == None
