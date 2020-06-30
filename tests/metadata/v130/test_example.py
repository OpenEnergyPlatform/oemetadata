def test_if_example_json_loads_successfully():
    from metadata.v130.example import OEMETADATA_V130_EXAMPLE


def test_example_against_schema_which_should_succeed():
    import jsonschema
    from metadata.v130.example import OEMETADATA_V130_EXAMPLE
    from metadata.v130.schema import OEMETADATA_V130_SCHEMA

    assert jsonschema.validate(OEMETADATA_V130_EXAMPLE, OEMETADATA_V130_SCHEMA) == None
