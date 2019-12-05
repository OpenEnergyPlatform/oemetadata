def test_if_schema_json_loads_successfully():
    from oemetadata.v140.schema import OEMETADATA_V140_SCHEMA


def test_if_schema_json_has_correct_schema_and_id_set():
    from oemetadata.v140.schema import OEMETADATA_V140_SCHEMA

    assert OEMETADATA_V140_SCHEMA["$schema"] == "http://json-schema.org/draft-07/schema#"
    assert (
        OEMETADATA_V140_SCHEMA["$id"]
        == "https://raw.githubusercontent.com/OpenEnergyPlatform/oemetadata/master/oemetadata/v140/schema.json"
    )


def test_schema_against_metaschema_which_should_succeed():
    import jsonschema
    from oemetadata.v140.schema import OEMETADATA_V140_SCHEMA
    from oemetadata.metaschema.draft07.schema import OEMETADATA_METASCHEMA_DRAFT07_SCHEMA

    assert (
        jsonschema.validate(OEMETADATA_V140_SCHEMA, OEMETADATA_METASCHEMA_DRAFT07_SCHEMA)
        == None
    )
