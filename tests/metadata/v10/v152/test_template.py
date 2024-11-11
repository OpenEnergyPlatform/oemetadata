def test_oemetadata_template_should_load():
    try:
        from metadata.v10.v152.template import OEMETADATA_V152_TEMPLATE
    except Warning:
        print("Cannot open OEMetadata Template (v1.5.2)!")


def test_oemetadata_schema_should_validate_oemetadata_template():
    from jsonschema import validate, ValidationError
    from metadata.v10.v152.template import OEMETADATA_V152_TEMPLATE
    from metadata.v10.v152.schema import OEMETADATA_V152_SCHEMA

    try:
        validate(OEMETADATA_V152_TEMPLATE, OEMETADATA_V152_SCHEMA)
        print("OEMetadata Template is valid OEMetadata Schema (v1.5.2).")
    except ValidationError as e:
        print("Cannot validate OEMetadata Template with Schema (v1.5.2)!", e)
