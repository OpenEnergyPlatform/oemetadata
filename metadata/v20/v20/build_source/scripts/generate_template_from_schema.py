#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# SPDX-FileCopyrightText: Ludwig Hülk <@Ludee> © Reiner Lemoine Institut
# SPDX-FileCopyrightText: Jonas Huber <jh-RLI> © Reiner Lemoine Institut
#
# SPDX-License-Identifier: MIT

"""
Title: Create template from schema
Description: Create template.json from schema.json.
Author: jh-RLI, Ludee
Email: jonas.huber@rl-institut.de
Date: 2024-05-30
Version: 1.0.0
"""

# Import

import json
import logging

from settings import RESOLVED_SCHEMA_FILE_NAME, TEMPLATE_PATH, LOG_FORMAT

# Configuration

logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)
logger = logging.getLogger(__name__)


def generate_template(schema):
    if isinstance(schema, bool):
        return {} if schema else None

    if "type" not in schema and "properties" not in schema and "items" not in schema:
        return None

    schema_type = schema.get("type")

    if isinstance(schema_type, list):
        schema_type = schema_type[0]

    template = None
    # Convert template string to actual type if necessary
    # if schema_type == "array" and isinstance(template, str):
    #     try:
    #         template = json.loads(template.replace("'", '"'))
    #     except json.JSONDecodeError:
    #         pass
    # return template

    if schema_type == "object" or "properties" in schema:
        template = {}
        properties = schema.get("properties", {})
        for prop, prop_schema in properties.items():
            template[prop] = generate_template(prop_schema)
        additional_properties = schema.get("additionalProperties", True)
        if isinstance(additional_properties, dict):
            template["additional_property"] = generate_template(additional_properties)
        return template

    if schema_type == "array":
        item_schema = schema.get("items", {})
        return [generate_template(item_schema)]

    if schema_type == "string":
        return ""

    if schema_type == "number":
        return 0

    if schema_type == "integer":
        return 0

    if schema_type == "boolean":
        return False

    return None


def main():
    schema_file_path = RESOLVED_SCHEMA_FILE_NAME

    with open(schema_file_path, "r", encoding="utf-8") as schema_file:
        schema = json.load(schema_file)

    template = generate_template(schema)

    template_file_path = TEMPLATE_PATH
    with open(template_file_path, "w", encoding="utf-8") as template_file:
        json.dump(template, template_file, indent=2, ensure_ascii=False)

    logger.info(f"template JSON generated and saved to {template_file_path}")

    # WARNING: The metaMetadata is missing and the boundingBox is wrong!

def test_oemetadata_schema_should_validate_oemetadata_template():
    from jsonschema import validate, ValidationError
    from metadata.v20.v20.template import OEMETADATA_V20_TEMPLATE
    from metadata.v20.v20.schema import OEMETADATA_V20_SCHEMA

    try:
        validate(OEMETADATA_V20_TEMPLATE, OEMETADATA_V20_SCHEMA)
        print("OEMetadata Template is valid OEMetadata Schema (v2.0).")
    except ValidationError as e:
        print("Cannot validate OEMetadata Template with Schema (v2.0)!", e)

def find_and_replace_key(data, target_key, new_value):
    if isinstance(data, dict):
        for key, value in data.items():
            if key == target_key:
                data[key] = new_value
                return True  # Return True if replacement is successful
            elif isinstance(value, (dict, list)):
                if find_and_replace_key(value, target_key, new_value):
                    return True  # Return True if replacement occurs in nested structure
    elif isinstance(data, list):
        for item in data:
            if find_and_replace_key(item, target_key, new_value):
                return True
    return False  # Return False if key not found

def replace_key_in_json(file_path, target_key, new_value):
    # Open and read the JSON file
    with open(file_path, 'r') as file:
        data = json.load(file)

    # Perform the key replacement
    if find_and_replace_key(data, target_key, new_value):
        # Save the updated JSON data back to the file
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"Updated '{target_key}' to '{new_value}' in {file_path}")
    else:
        print(f"Key '{target_key}' not found in JSON file.")


if __name__ == "__main__":
    logger.info("Generation started.")
    main()
    replace_key_in_json(TEMPLATE_PATH, 'boundingBox', [0, 0, 0, 0])
    replace_key_in_json(TEMPLATE_PATH, 'metadataVersion', 'OEMetadata-2.0.1')
    replace_key_in_json(TEMPLATE_PATH, 'metadataLicense', {
            "name": "CC0-1.0",
            "title": "Creative Commons Zero v1.0 Universal",
            "path": "https://creativecommons.org/publicdomain/zero/1.0"
        })
    test_oemetadata_schema_should_validate_oemetadata_template()
    logger.info("Generation ended.")
