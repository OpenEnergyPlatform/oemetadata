def test_if_example_json_loads_successfully():
    from metadata.v20.example import OEMETADATA_V200_EXAMPLE


def test_example_against_schema_which_should_succeed():
    import jsonschema
    from metadata.v20.example import OEMETADATA_V200_EXAMPLE
    from metadata.v20.schema import OEMETADATA_V200_SCHEMA

    assert jsonschema.validate(OEMETADATA_V200_EXAMPLE, OEMETADATA_V200_SCHEMA) == None
