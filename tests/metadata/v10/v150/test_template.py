def test_if_template_json_loads_successfully():
    from metadata.v150.template import OEMETADATA_V150_TEMPLATE


def test_template_against_schema_which_should_succeed():
    import jsonschema
    from metadata.v150.template import OEMETADATA_V150_TEMPLATE
    from metadata.v150.schema import OEMETADATA_V150_SCHEMA

    assert jsonschema.validate(OEMETADATA_V150_TEMPLATE, OEMETADATA_V150_SCHEMA) == None
