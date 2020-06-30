def test_if_template_json_loads_successfully():
    from metadata.v130.template import OEMETADATA_V130_TEMPLATE


def test_template_against_schema_which_should_succeed():
    import jsonschema
    from metadata.v130.template import OEMETADATA_V130_TEMPLATE
    from metadata.v130.schema import OEMETADATA_V130_SCHEMA

    assert jsonschema.validate(OEMETADATA_V130_TEMPLATE, OEMETADATA_V130_SCHEMA) == None
