def test_if_template_json_loads_successfully():
    from metadata.v140.template import OEMETADATA_V140_TEMPLATE


def test_template_against_schema_which_should_succeed():
    import jsonschema
    from metadata.v140.template import OEMETADATA_V140_TEMPLATE
    from metadata.v140.schema import OEMETADATA_V140_SCHEMA

    assert jsonschema.validate(OEMETADATA_V140_TEMPLATE, OEMETADATA_V140_SCHEMA) == None
