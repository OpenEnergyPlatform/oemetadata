def test_if_template_json_loads_successfully():
    from metadata.latest.template import OEMETADATA_LATEST_TEMPLATE


def test_template_against_schema_which_should_succeed():
    import jsonschema
    from metadata.latest.template import OEMETADATA_LATEST_TEMPLATE
    from metadata.latest.schema import OEMETADATA_LATEST_SCHEMA

    assert jsonschema.validate(OEMETADATA_LATEST_TEMPLATE, OEMETADATA_LATEST_SCHEMA) == None
