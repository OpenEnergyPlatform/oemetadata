def test_if_template_json_loads_successfully():
    from metadata.v141.template import OEMETADATA_V141_TEMPLATE


def test_template_against_schema_which_should_succeed():
    import jsonschema
    from metadata.v141.template import OEMETADATA_V141_TEMPLATE
    from metadata.v141.schema import OEMETADATA_V141_SCHEMA

    assert jsonschema.validate(OEMETADATA_V141_TEMPLATE, OEMETADATA_V141_SCHEMA) == None
