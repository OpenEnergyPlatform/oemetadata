def test_oemetadata_schema_should_load():
    try:
        from metadata.v10.v141.schema import OEMETADATA_V141_SCHEMA
    except Warning:
        print("Cannot open OEMetadata Schema (v1.4.1)!")


def test_jsonschema_should_validate_oemetadata_schema():
    from jsonschema import validate, ValidationError
    from metadata.v10.v141.schema import OEMETADATA_V141_SCHEMA
    from metadata.json_schema.draft07.schema \
        import OEMETADATA_JSONSCHEMA_DRAFT07_SCHEMA

    try:
        validate(OEMETADATA_V141_SCHEMA, OEMETADATA_JSONSCHEMA_DRAFT07_SCHEMA)
        print("OEMetadata Schema (v1.4.1) is valid JSON Schema.")
    except ValidationError as e:
        print("Cannot validate OEMetadata Schema with JSON Schema (v1.4.1)!", e)


def test_oemetadata_schema_should_have_correct_path():
    from metadata.v10.v141.schema import OEMETADATA_V141_SCHEMA
    import string

    def get_string(s):
        return string.printable + s + string.printable

    assert get_string(OEMETADATA_V141_SCHEMA["$schema"]) == get_string(
        "http://json-schema.org/draft-07/schema#"
    ), "Wrong schema path in OEMetadata Schema (v1.4.1)!"

    assert get_string(OEMETADATA_V141_SCHEMA["$id"]) == get_string(
        "https://raw.githubusercontent.com/OpenEnergyPlatform/oemetadata/production/metadata/v10/v141/schema.json"
    ), "Wrong id path in OEMetadata Schema (v1.4.1)!"
