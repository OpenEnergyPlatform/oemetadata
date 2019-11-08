def test_if_schema_json_loads_successfully():
    from metadata.v140.schema import METADATA_V140_SCHEMA


def test_if_schema_json_has_correct_schema_and_id_set():
    from metadata.v140.schema import METADATA_V140_SCHEMA

    assert METADATA_V140_SCHEMA["$schema"] == "http://json-schema.org/draft-07/schema#"
    assert (
        METADATA_V140_SCHEMA["$id"]
        == "https://raw.githubusercontent.com/OpenEnergyPlatform/metadata/master/metadata/v140/schema.json"
    )
