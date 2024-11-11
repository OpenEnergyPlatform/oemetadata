def test_oemetadata_example_should_load():
    try:
        from metadata.latest.example import OEMETADATA_LATEST_EXAMPLE
    except Warning:
        print("Cannot open OEMetadata Example (latest)!")


def test_oemetadata_schema_should_validate_oemetadata_example():
    from jsonschema import validate, ValidationError
    from metadata.latest.example import OEMETADATA_LATEST_EXAMPLE
    from metadata.latest.schema import OEMETADATA_LATEST_SCHEMA

    try:
        validate(OEMETADATA_LATEST_EXAMPLE, OEMETADATA_LATEST_SCHEMA)
        print("OEMetadata Example is valid OEMetadata Schema (latest).")
    except ValidationError as e:
        print("Cannot validate OEMetadata Example with Schema (latest)!", e)
