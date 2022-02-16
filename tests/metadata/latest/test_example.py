def test_if_example_json_loads_successfully():
    from metadata.latest.example import OEMETADATA_LATEST_EXAMPLE


def test_example_against_schema_which_should_succeed():
    import jsonschema
    from metadata.latest.example import OEMETADATA_LATEST_EXAMPLE
    from metadata.latest.schema import OEMETADATA_LATEST_SCHEMA

    assert jsonschema.validate(OEMETADATA_LATEST_EXAMPLE, OEMETADATA_LATEST_SCHEMA) == None
