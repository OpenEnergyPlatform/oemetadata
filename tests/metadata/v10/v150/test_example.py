def test_if_example_json_loads_successfully():
    from metadata.v150.example import OEMETADATA_V150_EXAMPLE


def test_example_against_schema_which_should_succeed():
    import jsonschema
    from metadata.v150.example import OEMETADATA_V150_EXAMPLE
    from metadata.v150.schema import OEMETADATA_V150_SCHEMA

    assert jsonschema.validate(OEMETADATA_V150_EXAMPLE, OEMETADATA_V150_SCHEMA) == None
