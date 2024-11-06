def test_oemetadata_schema_should_load():
    try:
        from metadata.v10.v130.schema import OEMETADATA_V130_SCHEMA
    except Warning:
        print("Cannot open OEMetadata Schema v1.3.0!")


def test_jsonschema_should_validate_oemetadata_schema():
    import jsonschema
    from metadata.v10.v130.schema import OEMETADATA_V130_SCHEMA
    from metadata.json_schema.draft07.schema \
        import OEMETADATA_JSONSCHEMA_DRAFT07_SCHEMA

    assert jsonschema.validate(OEMETADATA_V130_SCHEMA,
                               OEMETADATA_JSONSCHEMA_DRAFT07_SCHEMA) is None, \
        "Cannot validate OEMetadata Schema v1.3.0 with JSON schema (draft07)"


def test_oemetadata_schema_should_have_correct_path():
    from metadata.v10.v130.schema import OEMETADATA_V130_SCHEMA
    import string

    def get_string(s):
        return string.printable + s + string.printable

    assert get_string(OEMETADATA_V130_SCHEMA["$schema"]) == get_string(
        "http://json-schema.org/draft-07/schema#"
    ), "Wrong schema path in OEMetadata Schema v1.3.0!"

    assert get_string(OEMETADATA_V130_SCHEMA["$id"]) == get_string(
        "https://raw.githubusercontent.com/OpenEnergyPlatform/oemetadata/production/metadata/v130/schema.json"
    ), "Wrong id path in OEMetadata Schema v1.3.0!"


