def test_if_template_json_loads_successfully():
    from metadata.v151.template import OEMETADATA_V151_TEMPLATE


def test_template_against_schema_which_should_succeed():
    import jsonschema
    from metadata.v151.template import OEMETADATA_V151_TEMPLATE
    from metadata.v151.schema import OEMETADATA_V151_SCHEMA

    assert jsonschema.validate(OEMETADATA_V151_TEMPLATE, OEMETADATA_V151_SCHEMA) == None
