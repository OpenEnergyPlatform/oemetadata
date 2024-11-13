# SPDX-FileCopyrightText: Ludwig Hülk <@Ludee> © Reiner Lemoine Institut
# SPDX-FileCopyrightText: Jonas Huber <jh-RLI> © Reiner Lemoine Institut
#
# SPDX-License-Identifier: CC0-1.0

def test_jsonschema_should_load():
    try:
        from metadata.json_schema.draft2020_12.schema \
            import OEMETADATA_JSONSCHEMA_DRAFT202012_SCHEMA
    except Warning:
        print("Cannot open JSON Schema (draft2020-12)!")


def test_jsonschema_should_have_correct_path():
    from metadata.json_schema.draft2020_12.schema \
        import OEMETADATA_JSONSCHEMA_DRAFT202012_SCHEMA

    assert OEMETADATA_JSONSCHEMA_DRAFT202012_SCHEMA["$schema"] \
        == "https://json-schema.org/draft/2020-12/schema", \
        "Wrong schema path in JSON Schema (draft2020-12)!"

    assert OEMETADATA_JSONSCHEMA_DRAFT202012_SCHEMA["$id"] \
        == "https://json-schema.org/draft/2020-12/schema", \
        "Wrong id path in JSON Schema (draft2020-12)!"


def test_jsonschema_should_have_correct_path_string():
    from metadata.json_schema.draft2020_12.schema \
        import OEMETADATA_JSONSCHEMA_DRAFT202012_SCHEMA
    import string

    def get_string(s):
        return string.printable + s + string.printable

    assert get_string(OEMETADATA_JSONSCHEMA_DRAFT202012_SCHEMA["$schema"]) \
        == get_string("https://json-schema.org/draft/2020-12/schema"), \
        "Wrong schema path in JSON Schema (draft2020-12) with strings!"

    assert get_string(OEMETADATA_JSONSCHEMA_DRAFT202012_SCHEMA["$id"]) \
        == get_string("https://json-schema.org/draft/2020-12/schema"), \
        "Wrong id path in JSON Schema (draft2020-12) with strings!"
