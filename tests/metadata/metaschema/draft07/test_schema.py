def test_if_schema_json_loads_successfully():
    try:
        from metadata.metaschema.draft07.schema import OEMETADATA_METASCHEMA_DRAFT07_SCHEMA
    except Warning:
        print("Can´t load Metaschema. Check if the files are missing!")


def test_if_schema_json_has_correct_schema_and_id_set():
    from metadata.metaschema.draft07.schema import OEMETADATA_METASCHEMA_DRAFT07_SCHEMA

    assert OEMETADATA_METASCHEMA_DRAFT07_SCHEMA["$schema"] == "http://json-schema.org/draft-07/schema#"
    assert OEMETADATA_METASCHEMA_DRAFT07_SCHEMA["$id"] == "http://json-schema.org/draft-07/schema#"
