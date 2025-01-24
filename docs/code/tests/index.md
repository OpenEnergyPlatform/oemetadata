# Tests


## Test - Load File

`test_FILE_should_load`

!!! warning
    "Cannot open FILE!"

Solutions:
- Check if the **file path or name** is correct
- Check if the **test path or name** is correct


## Test - Validate Schema

### Validate OEMetadata Schema with JSON Schema

`test_jsonschema_should_validate_oemetadata_schema`

!!! warning
    "Cannot validate OEMetadata Schema with JSON Schema (VERSION)!"

Solutions:
- Check if correct JSON Schema has been used
- Check if OEMetadata Schema is valid


### Validate FILE with OEMetadata Schema

`test_oemetadata_schema_should_validate_FILE`

!!! warning
    "Cannot validate FILE with OEMetadata Schema (VERSION)!"

Solutions:
- Check if correct OEMetadata Schema has been used
- Check if OEMetadata Schema is valid
- Check if FILE is valid


## Test - Correct path

`test_FILE_should_have_correct_path`

!!! warning
    "Wrong path in FILE (VERSION)!"

Solutions:
- Check if path is correct
- Check if test path is correct
