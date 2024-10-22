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

import json
import logging

from typing import Any, Dict, Union, List

# from datetime import datetime
from pathlib import Path

from settings import VERSION_PATH, RESOLVED_SCHEMA_FILE_NAME, EXAMPLE_PATH, LOG_FORMAT

# Configuration
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)
logger = logging.getLogger(__name__)


def read_schema(filename: str) -> Dict[str, Any]:
    """Read a JSON schema from a file.

    Args:
        filename (str): The path to the JSON schema file.

    Returns:
        Dict[str, Any]: The JSON schema as a dictionary.
    """

    with open(VERSION_PATH / filename, "r", encoding="utf-8") as file:
        schema = json.load(file)
    return schema


def generate_example(
    schema: Dict[str, Any]
) -> Union[Dict[str, Any], List[Any], str, None]:
    """Generate a JSON object from the schema using the example values provided.

    Args:
        schema (Dict[str, Any]): The JSON schema.

    Returns:
        Union[Dict[str, Any], List[Any], str, None]: A JSON object generated from the schema.
    """
    if "example" in schema:
        return schema["example"]

    schema_type = schema.get("type", None)
    if isinstance(schema_type, list):
        schema_type = schema_type[0]

    if schema_type == "object":
        example_object = {}
        properties = schema.get("properties", {})
        for key, value in properties.items():
            example_object[key] = generate_example(value)
        return example_object

    elif schema_type == "array":
        items = schema.get("items", {})
        return [generate_example(items)]

    elif schema_type == "string":
        return ""

    elif schema_type == "null":
        return None

    return None


def generate_json_from_schema(schema_file: str) -> Dict[str, Any]:
    """Generate a JSON object that conforms to the schema read from a file.

    Args:
        schema_file (str): The path to the JSON schema file.

    Returns:
        Dict[str, Any]: A JSON object generated from the schema.
    """
    schema = read_schema(schema_file)
    return generate_example(schema)


def save_json(data: Dict[str, Any], filename: Path) -> None:
    """Save the given data as a JSON file.

    Args:
        data (Dict[str, Any]): The JSON data to be saved.
        filename (str): The filename where the JSON data will be saved.
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    schema_filename = RESOLVED_SCHEMA_FILE_NAME
    json_data = generate_json_from_schema(schema_filename)
    save_json(json_data, EXAMPLE_PATH)
