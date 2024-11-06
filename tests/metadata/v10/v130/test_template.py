def test_oemetadata_template_should_load():
    try:
        from metadata.v10.v130.template import OEMETADATA_V130_TEMPLATE
    except Warning:
        print("Cannot open OEMetadata Template v1.3.0!")


def test_jsonschema_should_validate_oemetadata_template():
    import jsonschema
    from metadata.v10.v130.template import OEMETADATA_V130_TEMPLATE
    from metadata.v10.v130.schema import OEMETADATA_V130_SCHEMA

    assert jsonschema.validate(OEMETADATA_V130_TEMPLATE,
                               OEMETADATA_V130_SCHEMA) is None, \
        "Cannot validate OEMetadata Template v1.3.0 with JSON schema (draft07)"
