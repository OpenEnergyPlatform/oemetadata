def test_if_template_json_loads_successfully():
    from metadata.v20.template import OEMETADATA_V200_TEMPLATE


def test_template_against_schema_which_should_succeed():
    import jsonschema
    from metadata.v20.template import OEMETADATA_V200_TEMPLATE
    from metadata.v20.schema import OEMETADATA_V200_SCHEMA

    assert jsonschema.validate(OEMETADATA_V200_TEMPLATE, OEMETADATA_V200_SCHEMA) == None
