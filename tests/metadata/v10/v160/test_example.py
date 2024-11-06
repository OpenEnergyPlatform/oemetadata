def test_if_example_json_loads_successfully():
    from metadata.v160.example import OEMETADATA_V160_EXAMPLE


def test_example_against_schema_which_should_succeed():
    import jsonschema
    from metadata.v160.example import OEMETADATA_V160_EXAMPLE
    from metadata.v160.schema import OEMETADATA_V160_SCHEMA

    assert jsonschema.validate(OEMETADATA_V160_EXAMPLE, OEMETADATA_V160_SCHEMA) == None
