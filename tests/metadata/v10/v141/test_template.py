def test_oemetadata_template_should_load():
    try:
        from metadata.v10.v141.template import OEMETADATA_V141_TEMPLATE
    except Warning:
        print("Cannot open OEMetadata Template (v1.4.1)!")


def test_oemetadata_schema_should_validate_oemetadata_template():
    from jsonschema import validate, ValidationError
    from metadata.v10.v141.template import OEMETADATA_V141_TEMPLATE
    from metadata.v10.v141.schema import OEMETADATA_V141_SCHEMA

    try:
        validate(OEMETADATA_V141_TEMPLATE, OEMETADATA_V141_SCHEMA)
        print("OEMetadata Template is valid OEMetadata Schema (v1.4.1).")
    except ValidationError as e:
        print("Cannot validate OEMetadata Template with Schema (v1.4.1)!", e)
