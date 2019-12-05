def test_if_schema_json_loads_successfully():
    from oemetadata.metaschema.draft07.schema import OEMETADATA_METASCHEMA_DRAFT07_SCHEMA


def test_if_schema_json_has_correct_schema_and_id_set():
    from oemetadata.metaschema.draft07.schema import OEMETADATA_METASCHEMA_DRAFT07_SCHEMA

    assert (
        OEMETADATA_METASCHEMA_DRAFT07_SCHEMA["$schema"]
        == "http://json-schema.org/draft-07/schema#"
    )
    assert (
        OEMETADATA_METASCHEMA_DRAFT07_SCHEMA["$id"]
        == "http://json-schema.org/draft-07/schema#"
    )
