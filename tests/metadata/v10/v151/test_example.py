def test_oemetadata_example_should_load():
    try:
        from metadata.v10.v151.example import OEMETADATA_V151_EXAMPLE
    except Warning:
        print("Cannot open OEMetadata Example v1.5.1!")


def test_oemetadata_schema_should_validate_oemetadata_example():
    from jsonschema import validate, ValidationError
    from metadata.v10.v151.example import OEMETADATA_V151_EXAMPLE
    from metadata.v10.v151.schema import OEMETADATA_V151_SCHEMA

    try:
        validate(OEMETADATA_V151_EXAMPLE, OEMETADATA_V151_SCHEMA)
        print("OEMetadata Example is valid OEMetadata Schema (v1.5.1).")
    except ValidationError as e:
        print("Cannot validate OEMetadata Example with Schema (v1.5.1)!", e)
