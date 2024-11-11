def test_jsonschema_should_load():
    try:
        from metadata.json_schema.draft07.schema \
            import OEMETADATA_JSONSCHEMA_DRAFT07_SCHEMA
    except Warning:
        print("Cannot open JSON Schema (draft07)!")


def test_jsonschema_should_have_correct_path():
    from metadata.json_schema.draft07.schema \
        import OEMETADATA_JSONSCHEMA_DRAFT07_SCHEMA

    assert OEMETADATA_JSONSCHEMA_DRAFT07_SCHEMA["$schema"] \
        == "http://json-schema.org/draft-07/schema#", \
        "Wrong schema path in JSON Schema (draft07)!"

    assert OEMETADATA_JSONSCHEMA_DRAFT07_SCHEMA["$id"] \
        == "http://json-schema.org/draft-07/schema#", \
        "Wrong id path in JSON Schema (draft07)!"
