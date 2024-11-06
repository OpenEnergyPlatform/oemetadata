def test_if_example_json_loads_successfully():
    from metadata.v151.example import OEMETADATA_V151_EXAMPLE


def test_example_against_schema_which_should_succeed():
    import jsonschema
    from metadata.v151.example import OEMETADATA_V151_EXAMPLE
    from metadata.v151.schema import OEMETADATA_V151_SCHEMA

    assert jsonschema.validate(OEMETADATA_V151_EXAMPLE, OEMETADATA_V151_SCHEMA) == None
