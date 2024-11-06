def test_oemetadata_example_should_load():
    try:
        from metadata.v10.v130.example import OEMETADATA_V130_EXAMPLE
    except Warning:
        print("Cannot open OEMetadata Example v1.3.0!")


def test_jsonschema_should_validate_oemetadata_example():
    import jsonschema
    from metadata.v10.v130.example import OEMETADATA_V130_EXAMPLE
    from metadata.v10.v130.schema import OEMETADATA_V130_SCHEMA

    assert jsonschema.validate(OEMETADATA_V130_EXAMPLE,
                               OEMETADATA_V130_SCHEMA) is None, \
        "Cannot validate OEMetadata Example v1.3.0 with JSON schema (draft07)"
