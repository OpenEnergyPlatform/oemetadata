def test_if_template_json_loads_successfully():
    from metadata.V160.template import OEMETADATA_V160_TEMPLATE


def test_template_against_schema_which_should_succeed():
    import jsonschema
    from metadata.V160.template import OEMETADATA_V160_TEMPLATE
    from metadata.V160.schema import OEMETADATA_V160_SCHEMA

    assert jsonschema.validate(OEMETADATA_V160_TEMPLATE, OEMETADATA_V160_SCHEMA) == None
