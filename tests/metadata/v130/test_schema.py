import jsonschema


def test_if_schema_json_loads_successfully():
    from metadata.v130.schema import METADATA_V130_SCHEMA


def test_schema_against_example_which_should_succeed():
    from metadata.v130.schema import METADATA_V130_SCHEMA
    from metadata.v130.example import METADATA_V130_EXAMPLE

    assert jsonschema.validate(METADATA_V130_EXAMPLE, METADATA_V130_SCHEMA) == None
