def test_if_example_json_loads_successfully():
    from metadata.v200_draft.example import OEMETADATA_V200_EXAMPLE


def test_example_against_schema_which_should_succeed():
    import jsonschema
    from metadata.v200_draft.example import OEMETADATA_V200_EXAMPLE
    from metadata.v200_draft.schema import OEMETADATA_V200_SCHEMA

    assert jsonschema.validate(OEMETADATA_V200_EXAMPLE, OEMETADATA_V200_SCHEMA) == None
