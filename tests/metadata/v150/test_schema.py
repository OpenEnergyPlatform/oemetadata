def test_if_schema_json_loads_successfully():
    try:
        from metadata.v150.schema import OEMETADATA_V150_SCHEMA
    except Warning:
        print("Metadata Schema v1.5.0 cant load. Check if the files are missing!")


def test_if_schema_json_has_correct_schema_and_id_set():
    from metadata.v150.schema import OEMETADATA_V150_SCHEMA
    import string

    def get_string(s):
        return string.printable + s + string.printable

    assert get_string(OEMETADATA_V150_SCHEMA["$schema"]) == get_string("http://json-schema.org/draft-07/schema#")

    # https://raw.githubusercontent.com/OpenEnergyPlatform/oemetadata/master/oemetadata/v150/schema.json
    assert get_string(OEMETADATA_V150_SCHEMA["$id"]) == get_string(
        "https://raw.githubusercontent.com/OpenEnergyPlatform/oemetadata/bf957f1f413e2dcd12a598b8101acd55354f0d5c/metadata/v150/schema.json"
    )


def test_schema_against_metaschema_which_should_succeed():
    import jsonschema
    from metadata.v150.schema import OEMETADATA_V150_SCHEMA
    from metadata.metaschema.draft07.schema import OEMETADATA_METASCHEMA_DRAFT07_SCHEMA

    assert jsonschema.validate(OEMETADATA_V141_SCHEMA, OEMETADATA_METASCHEMA_DRAFT07_SCHEMA) is None
