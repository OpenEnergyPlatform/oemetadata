def test_if_template_json_loads_successfully():
    from metadata.v152.template import OEMETADATA_V152_TEMPLATE


def test_template_against_schema_which_should_succeed():
    import jsonschema
    from metadata.v152.template import OEMETADATA_V152_TEMPLATE
    from metadata.v152.schema import OEMETADATA_V152_SCHEMA

    assert jsonschema.validate(OEMETADATA_V152_TEMPLATE, OEMETADATA_V152_SCHEMA) == None
