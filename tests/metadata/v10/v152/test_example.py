def test_if_example_json_loads_successfully():
    from metadata.v152.example import OEMETADATA_V152_EXAMPLE


def test_example_against_schema_which_should_succeed():
    import jsonschema
    from metadata.v152.example import OEMETADATA_V152_EXAMPLE
    from metadata.v152.schema import OEMETADATA_V152_SCHEMA

    assert jsonschema.validate(OEMETADATA_V152_EXAMPLE, OEMETADATA_V152_SCHEMA) == None
