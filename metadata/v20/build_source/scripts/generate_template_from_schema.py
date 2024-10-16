#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Title: create template from json schema
Description: Create template from json schema.
Author: jh-RLI
Email: jonas.huber@rl-institut.de
Date: 2024-05-30
Version: 1.0.0
"""

# Standard Library Imports
# import os
from os.path import dirname

import sys
import json
import logging

# from datetime import datetime
from pathlib import Path

from jsonschema import validate, ValidationError

# Configuration
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)
logger = logging.getLogger(__name__)

# Constants
BASE_PATH = Path("metadata/")
VERSION = "v20"
VERSION_PATH = BASE_PATH / VERSION
SCHEMA_BUILD_PATH = VERSION_PATH / "build_source"
MAIN_SCHEMA_PATH = SCHEMA_BUILD_PATH / "schema_structure.json"
SCHEMA_REFS = SCHEMA_BUILD_PATH / "schemas"
RESOLVED_SCHEMA_FILE_NAME = VERSION_PATH / "schema.json"
EXPECTED_SCHEMA_PATH = VERSION_PATH / "schema.json"
TEMPLATE_PATH = VERSION_PATH / "template.json"


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

    print(f"template JSON generated and saved to {template_file_path}")


if __name__ == "__main__":
    main()
