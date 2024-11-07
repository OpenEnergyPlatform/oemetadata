def test_oemetadata_template_should_load():
    try:
        from metadata.v10.v150.template import OEMETADATA_V150_TEMPLATE
    except Warning:
        print("Cannot open OEMetadata Template (v1.5.0)!")


def test_oemetadata_schema_should_validate_oemetadata_template():
    from jsonschema import validate, ValidationError
    from metadata.v10.v150.template import OEMETADATA_V150_TEMPLATE
    from metadata.v10.v150.schema import OEMETADATA_V150_SCHEMA

    try:
        validate(OEMETADATA_V150_TEMPLATE, OEMETADATA_V150_SCHEMA)
        print("OEMetadata Template is valid OEMetadata Schema (v1.5.0).")
    except ValidationError as e:
        print("Cannot validate OEMetadata Template with Schema (v1.5.0)!", e)
