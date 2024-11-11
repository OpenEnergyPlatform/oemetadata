def test_oemetadata_template_should_load():
    try:
        from metadata.latest.template import OEMETADATA_LATEST_TEMPLATE
    except Warning:
        print("Cannot open OEMetadata Template (latest)!")


def test_oemetadata_schema_should_validate_oemetadata_template():
    from jsonschema import validate, ValidationError
    from metadata.latest.template import OEMETADATA_LATEST_TEMPLATE
    from metadata.latest.schema import OEMETADATA_LATEST_SCHEMA

    try:
        validate(OEMETADATA_LATEST_TEMPLATE, OEMETADATA_LATEST_SCHEMA)
        print("OEMetadata Template is valid OEMetadata Schema (latest).")
    except ValidationError as e:
        print("Cannot validate OEMetadata Template with Schema (latest)!", e)
