#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Title: create example from json schema
Description: Create example from json schema.
Author: jh-RLI, Ludee
Email: jonas.huber@rl-institut.de
Date: 2024-05-30
Version: 1.0.0
"""

# Standard Library Imports
# import os

import json
import logging
import os

from typing import Any, Dict, Union, List
from pathlib import Path
from settings import RESOLVED_SCHEMA_FILE_NAME, EXAMPLE_PATH, LOG_FORMAT

# Configuration
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)
logger = logging.getLogger(__name__)


def read_schema(filepath: str) -> Dict[str, Any]:
    """Read a JSON schema from a file.

    Args:
        filepath (str): The path to the JSON schema file.

    Returns:
        Dict[str, Any]: The JSON schema as a dictionary.
    """

    with open(filepath, "r", encoding="utf-8") as file:
        schema = json.load(file)
    print(f"Processing schema: {schema}")
    return schema


def read_metadata_schema(filepath: str) -> Dict[str, Any]:
    """Read a JSON schema from a file.

    Args:
        filepath (str): The path to the JSON schema file.

    Returns:
        Dict[str, Any]: The JSON schema as a dictionary.
    """
    if not os.path.exists(filepath):
        print(f"Error: File '{filepath}' does not exist.")
        return {}

    try:
        with open(filepath, "r", encoding="utf-8") as file:
            schema = json.load(file)

        # Basic validation of schema structure
        if not isinstance(schema, dict):
            print("Error: Schema is not a dictionary. Check the schema format.")
            return {}

        print(f"Schema loaded successfully from {filepath}")
        print(f"Schema top-level keys: {list(schema.keys())}")

        # Additional debugging info: Check expected keys
        if "$schema" not in schema or "type" not in schema:
            print(
                "Warning: Schema may be missing key fields like '$schema' or 'type'.")

        print(
            f"Full schema content (trimmed for large files): {str(schema)[:500]}...")

        return schema

    except json.JSONDecodeError as e:
        print(f"Error reading JSON: {e}")
        return {}
    except Exception as e:
        print(f"An unexpected error occurred while reading the schema: {e}")
        return {}


def generate_example_old(
    schema: Dict[str, Any]
) -> Union[Dict[str, Any], List[Any], str, None]:
    """Generate a JSON object from the schema using the
    example values provided.

    Args:
        schema (Dict[str, Any]): The JSON schema.

    Returns:
        Union[Dict[str, Any], List[Any], str, None]:
            A JSON object generated from the schema.
    """
    if "examples" in schema:
        return schema["examples"]

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

        # Fix: Avoid double-wrapping by checking if the generated
        # example is already a list
        example = generate_example(items)

        if isinstance(example, list):
            return example  # If it's already a list, return it directly
        else:
            return [example]  # Otherwise, wrap it in a list

    elif schema_type == "string":
        return ""

    elif schema_type == "null":
        return None

    return None


def extract_examples_from_schema(schema: Dict[str, Any]) -> Union[
    Dict[str, Any], List[Any], str, None]:
    """Generate a valid example from the schema using the provided example values."""

    # If the schema has an "examples" field, handle it appropriately
    if "examples" in schema:
        examples = schema["examples"]
        if isinstance(examples, list):
            # Return a single value if the list contains one item
            if len(examples) == 1:
                return examples[0]
            return examples  # If multiple items, return the whole list
        return examples  # If it's a single item, return the value

    # If the schema type is an object, process each property recursively
    schema_type = schema.get("type")
    if isinstance(schema_type, list):
        schema_type = schema_type[0]

    if schema_type == "object":
        example_object = {}
        properties = schema.get("properties", {})
        for key, value in properties.items():
            example_object[key] = extract_examples_from_schema(value)
        return example_object

    # If the schema type is an array, process the items recursively
    elif schema_type == "array":
        items = schema.get("items", {})
        example = extract_examples_from_schema(items)
        return [example] if not isinstance(example, list) else example

    # Handle basic types like string, number, boolean, null
    elif schema_type == "string":
        return ""  # Example string
    elif schema_type == "number":
        return 0  # Example number
    elif schema_type == "boolean":
        return True  # Example boolean
    elif schema_type == "null":
        return None  # Example null

    return None  # Default fallback


def create_json_from_schema(schema_file: str) -> Dict[str, Any]:
    """Generate a JSON object that conforms to the schema read from a file.

    Args:
        schema_file (str): The path to the JSON schema file.

    Returns:
        Dict[str, Any]: A JSON object generated from the schema.
    """
    schema = read_metadata_schema(schema_file)
    print(f"Create JSON from schema: {schema_file}")
    return extract_examples_from_schema(schema)
    print(f"Create JSON object: {result}")


def save_json(data: Dict[str, Any], filename: Path) -> None:
    """Save the given data as a JSON file.

    Args:
        data (Dict[str, Any]): The JSON data to be saved.
        filename (str): The filename where the JSON data will be saved.
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

    logger.info(f"example JSON generated and saved to {filename}")

def test_oemetadata_schema_should_validate_oemetadata_example(example):
    from jsonschema import validate, ValidationError
    from metadata.v20.v20.schema import OEMETADATA_V20_SCHEMA

    try:
        validate(example, OEMETADATA_V20_SCHEMA)
        print("OEMetadata Example is valid OEMetadata Schema (v2.0).")
    except ValidationError as e:
        print("Cannot validate OEMetadata Example with Schema (v2.0)!", e)


if __name__ == "__main__":
    logger.info("Create OEMetadata Example from Schema.")
    schema_filename = RESOLVED_SCHEMA_FILE_NAME
    json_data = create_json_from_schema(schema_filename)
    save_json(json_data, EXAMPLE_PATH)
    logger.info("OEMetadata Example created!")
    test_oemetadata_schema_should_validate_oemetadata_example(json_data)
