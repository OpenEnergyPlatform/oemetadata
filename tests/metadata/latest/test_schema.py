def test_oemetadata_schema_should_load():
    try:
        from metadata.latest.schema import OEMETADATA_LATEST_SCHEMA
    except Warning:
        print("Cannot open OEMetadata Schema (Latest)!")


def test_jsonschema_should_validate_oemetadata_schema():
    from jsonschema import validate, ValidationError
    from metadata.latest.schema import OEMETADATA_LATEST_SCHEMA
    from metadata.json_schema.draft07.schema \
        import OEMETADATA_JSONSCHEMA_DRAFT07_SCHEMA

    try:
        validate(OEMETADATA_LATEST_SCHEMA, OEMETADATA_JSONSCHEMA_DRAFT07_SCHEMA)
        print("OEMetadata Schema (Latest) is valid JSON Schema.")
    except ValidationError as e:
        print("Cannot validate OEMetadata Schema with JSON Schema (Latest)!", e)


def test_oemetadata_schema_should_have_correct_path():
    from metadata.latest.schema import OEMETADATA_LATEST_SCHEMA
    import string

    def get_string(s):
        return string.printable + s + string.printable

    assert get_string(OEMETADATA_LATEST_SCHEMA["$schema"]) == get_string(
        "http://json-schema.org/draft-07/schema#"
    ), "Wrong schema path in OEMetadata Schema Latest!"

    assert get_string(OEMETADATA_LATEST_SCHEMA["$id"]) == get_string(
        "https://raw.githubusercontent.com/OpenEnergyPlatform/oemetadata/production/metadata/v10/latest/schema.json"
    ), "Wrong id path in OEMetadata Schema Latest!"
