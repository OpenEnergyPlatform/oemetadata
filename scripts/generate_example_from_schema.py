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
SCHEMA_BUILD_PATH = VERSION_PATH / "build"
MAIN_SCHEMA_PATH = SCHEMA_BUILD_PATH / "main_schema.json"
SCHEMA_REFS = SCHEMA_BUILD_PATH / "schemas"
RESOLVED_SCHEMA_FILE_NAME = VERSION_PATH / "res_schema.json"
EXPECTED_SCHEMA_PATH = VERSION_PATH / "schema.json"
EXAMPLE_PATH = VERSION_PATH / "resolved_example.json"


def generate_example(schema):
    if "example" in schema:
        return schema["example"]
    if "const" in schema:
        return schema["const"]
    if "enum" in schema:
        return schema["enum"][0]
    if schema.get("type") == "object":
        obj = {}
        for key, value in schema.get("properties", {}).items():
            obj[key] = generate_example(value)
        return obj
    if schema.get("type") == "array":
        example_items = schema.get("example", [])
        if not example_items:
            example_items = [generate_example(schema["items"])]
        return example_items
    if "type" in schema:
        if schema["type"] == "string":
            return schema.get("example", "")
        if schema["type"] == "number":
            return schema.get("example", 0)
        if schema["type"] == "boolean":
            return schema.get("example", False)
        if schema["type"] == "null":
            return None
    return None


def create_example_json(schema_file_path, output_file_path):
    with open(schema_file_path, "r") as schema_file:
        schema = json.load(schema_file)

    example_json = generate_example(schema)

    with open(output_file_path, "w") as output_file:
        json.dump(example_json, output_file, indent=4)
    print(f"{output_file_path} has been created.")

    try:
        validate(instance=example_json, schema=schema)
        print(f"The generated example JSON is valid according to the schema.")
    except ValidationError as e:
        print(f"The generated example JSON is not valid: {e.message}")


schema_file_path = RESOLVED_SCHEMA_FILE_NAME
output_file_path = EXAMPLE_PATH

create_example_json(schema_file_path, output_file_path)
