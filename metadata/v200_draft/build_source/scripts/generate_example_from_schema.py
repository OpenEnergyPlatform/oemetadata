#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Title: create example from json schema
Description: Create example from json schema.
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
VERSION = "v200_draft"
VERSION_PATH = BASE_PATH / VERSION
SCHEMA_BUILD_PATH = VERSION_PATH / "build_source"
MAIN_SCHEMA_PATH = SCHEMA_BUILD_PATH / "schema_structure.json"
SCHEMA_REFS = SCHEMA_BUILD_PATH / "schemas"
RESOLVED_SCHEMA_FILE_NAME = VERSION_PATH / "schema.json"
EXPECTED_SCHEMA_PATH = VERSION_PATH / "schema.json"
EXAMPLE_PATH = VERSION_PATH / "resolved_example.json"


def generate_example(schema):
    if isinstance(schema, bool):
        return {} if schema else None

    if "type" not in schema and "properties" not in schema and "items" not in schema:
        return None

    schema_type = schema.get("type")

    if isinstance(schema_type, list):
        schema_type = schema_type[0]

    if "example" in schema:
        example = schema["example"]
        # Convert example string to actual type if necessary
        if schema_type == "array" and isinstance(example, str):
            try:
                example = json.loads(example.replace("'", '"'))
            except json.JSONDecodeError:
                pass
        return example

    if schema_type == "object" or "properties" in schema:
        example = {}
        properties = schema.get("properties", {})
        for prop, prop_schema in properties.items():
            example[prop] = generate_example(prop_schema)
        additional_properties = schema.get("additionalProperties", True)
        if isinstance(additional_properties, dict):
            example["additional_property"] = generate_example(additional_properties)
        return example

    if schema_type == "array":
        item_schema = schema.get("items", {})
        return [generate_example(item_schema)]

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

    with open(schema_file_path, "r",  encoding="utf-8") as schema_file:
        schema = json.load(schema_file)

    example = generate_example(schema)

    example_file_path = EXAMPLE_PATH
    with open(example_file_path, "w",  encoding="utf-8") as example_file:
        json.dump(example, example_file, indent=2, ensure_ascii=False)

    print(f"Example JSON generated and saved to {example_file_path}")


if __name__ == "__main__":
    main()
