def test_if_template_json_loads_successfully():
    from metadata.v140.template import METADATA_V140_TEMPLATE


def test_template_against_schema_which_should_succeed():
    import jsonschema
    from metadata.v140.template import METADATA_V140_TEMPLATE
    from metadata.v140.schema import METADATA_V140_SCHEMA

    assert jsonschema.validate(METADATA_V140_TEMPLATE, METADATA_V140_SCHEMA) == None
