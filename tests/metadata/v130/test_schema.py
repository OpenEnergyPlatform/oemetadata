def test_if_schema_json_loads_successfully():
    try:
        from metadata.v130.schema import OEMETADATA_V130_SCHEMA
    except Warning:
        print("Metadata Schema v1.3.0 cant load. Check if the files are missing!")


def test_if_schema_json_has_correct_schema_and_id_set():
    from metadata.v130.schema import OEMETADATA_V130_SCHEMA
    import string

    def get_string(s):
        return string.printable + s + string.printable

    assert get_string(OEMETADATA_V130_SCHEMA["$schema"]) == get_string("http://json-schema.org/draft-07/schema#")

    assert get_string(OEMETADATA_V130_SCHEMA["$id"]) == get_string(
        "https://raw.githubusercontent.com/OpenEnergyPlatform/oemetadata/master/oemetadata/v130/schema.json"
    )


def test_schema_against_metaschema_which_should_succeed():
    import jsonschema
    from metadata.v130.schema import OEMETADATA_V130_SCHEMA
    from metadata.metaschema.draft07.schema import OEMETADATA_METASCHEMA_DRAFT07_SCHEMA

    assert jsonschema.validate(OEMETADATA_V130_SCHEMA, OEMETADATA_METASCHEMA_DRAFT07_SCHEMA) is None
