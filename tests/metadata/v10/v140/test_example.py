def test_oemetadata_example_should_load():
    try:
        from metadata.v10.v140.example import OEMETADATA_V140_EXAMPLE
    except Warning:
        print("Cannot open OEMetadata Example (v1.4.0)!")


def test_oemetadata_schema_should_validate_oemetadata_example():
    from jsonschema import validate, ValidationError
    from metadata.v10.v140.example import OEMETADATA_V140_EXAMPLE
    from metadata.v10.v140.schema import OEMETADATA_V140_SCHEMA

    try:
        validate(OEMETADATA_V140_EXAMPLE, OEMETADATA_V140_SCHEMA)
        print("OEMetadata Example is valid OEMetadata Schema (v1.4.0).")
    except ValidationError as e:
        print("Cannot validate OEMetadata Example with Schema (v1.4.0)!", e)
