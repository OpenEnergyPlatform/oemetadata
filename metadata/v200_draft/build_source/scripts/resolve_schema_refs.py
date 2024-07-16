#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Title: Resolve schema $ref
Description: Resolve "$ref" elements in schema.json.
Author: jh-RLI
Email: jonas.huber@rl-institut.de
Date: 2024-05-30
Version: 1.0.0

requires: "pip install jsonschema referencing"

Usage: Script with additional arguments --debug for more detailed output. 
        Requires the folder structure introduced in oemetadata v2.0.0.
"""

# Standard Library Imports
# import os
import sys
import json
import logging

# from datetime import datetime
from pathlib import Path
from urllib.parse import urljoin
import argparse

from referencing import Registry, Resource
from jsonschema import Draft7Validator

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


# Function Definitions
def setup():
    """
    Setup function to initialize resources or configurations.
    """
    logger.info("Setup complete.")


# Load the main schema
def load_schema(schema_path):
    with open(schema_path, "r", encoding="utf-8") as file:
        return json.load(file)


# Ensure the schema has the $schema field
def ensure_schema_field(schema):
    if "$schema" not in schema:
        schema["$schema"] = "http://json-schema.org/draft-07/schema#"
    return schema


# Debugging function to print registry contents
def print_registry_contents(registry, debug):
    if debug:
        print("Registry Contents:")
        for uri, resource in registry._resources.items():
            print(f"{uri}: {resource.contents}")


# Resolve and merge references using referencing library
def resolve_and_merge(schema_path, debug):
    schema = load_schema(schema_path)
    schema = ensure_schema_field(schema)

    # Create a registry and register the schemas
    base_uri = MAIN_SCHEMA_PATH.resolve().parent.as_uri() + "/"
    registry = Registry().with_resource(base_uri, Resource.from_contents(schema))

    for schema_file in SCHEMA_REFS.glob("*.json"):
        try:
            with open(schema_file, "r") as file:
                ref_schema = json.load(file)
                ref_schema = ensure_schema_field(ref_schema)
                schema_uri = urljoin(base_uri, schema_file.name)
                registry = registry.with_resource(
                    schema_uri, Resource.from_contents(ref_schema)
                )
        except json.JSONDecodeError as e:
            logger.error(f"Error decoding JSON from {schema_file}: {e}")
            continue

    # Print registry contents for debugging
    print_registry_contents(registry, debug)

    # Resolve references in the schema
    def resolve_references(schema, registry, base_uri):
        if isinstance(schema, dict):
            if "$ref" in schema:
                ref_uri = urljoin(base_uri, schema["$ref"])
                if debug:
                    print(f"Resolving reference {ref_uri}")  # Debugging
                try:
                    ref_schema = registry[ref_uri]
                    if debug:
                        print(
                            f"Resolved reference {ref_uri} to {ref_schema.contents}"
                        )  # Debugging
                    return ref_schema.contents[
                        "properties"
                    ]  # Return only the properties
                except KeyError as e:
                    raise ValueError(f"Reference {ref_uri} could not be resolved: {e}")
            else:
                return {
                    key: resolve_references(value, registry, base_uri)
                    for key, value in schema.items()
                }
        elif isinstance(schema, list):
            return [resolve_references(item, registry, base_uri) for item in schema]
        return schema

    # Resolve the top-level properties
    def resolve_top_level_properties(schema, registry, base_uri):
        resolved_properties = {}
        for prop, value in schema["properties"].items():
            if isinstance(value, dict) and "properties" in value:
                resolved_value = resolve_references(
                    value["properties"], registry, base_uri
                )
                resolved_properties[prop] = resolved_value
            else:
                resolved_value = resolve_references(value, registry, base_uri)
                for i, v in resolved_value.items():
                    if isinstance(v, dict) and i != "items":
                        resolved_properties[i] = v

                    elif prop == "resources":
                        resolved_value = resolve_references(value, registry, base_uri)
                        resources = {}
                        for _k, _v in resolved_value["items"].items():
                            resources.update(_v)
                        resolved_properties[prop] = resources

                    else:
                        resolved_properties[prop] = resolved_value
        return resolved_properties

    schema["properties"] = resolve_top_level_properties(schema, registry, base_uri)
    return schema


#  if isinstance(value, dict) and "properties" in value:
#     resolved_value = resolve_references(
#         value["properties"], registry, base_uri
#     )
#     resolved_properties[prop] = resolved_value
# elif prop == "resources":
#     resolved_value = resolve_references(value, registry, base_uri)
#     for k,v in resolved_value["items"].items():
#         resolved_properties.update(v)


# else:
#     resolved_value = resolve_references(value, registry, base_uri)
#     resolved_properties[prop] = resolved_value
# Validate the schema
def validate_schema(resolved_schema, expected_schema):
    validator = Draft7Validator(expected_schema)
    errors = sorted(validator.iter_errors(resolved_schema), key=lambda e: e.path)
    for error in errors:
        print(f"Validation error at {list(error.path)}: {error.message}")


# Load expected schema (without refs) for validation
def load_expected_schema(expected_schema_path):
    with open(expected_schema_path, "r", encoding="utf-8") as file:
        return json.load(file)


def main(debug):
    """
    Main function to execute the script's primary logic.
    """
    try:
        setup()
        logger.info("Main execution started.")

        # Resolve and merge the schema
        resolved_schema = resolve_and_merge(MAIN_SCHEMA_PATH, debug)

        # Save the resolved schema to a new file
        with open(RESOLVED_SCHEMA_FILE_NAME, "w", encoding="utf-8") as output_file:
            json.dump(resolved_schema, output_file, indent=2)

        # Load the expected schema and validate
        expected_schema = load_expected_schema(EXPECTED_SCHEMA_PATH)
        validate_schema(resolved_schema, expected_schema)

        logger.info("Main execution finished.")
    except Exception as e:
        logger.error("An error occurred: %s", e)
        sys.exit(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Resolve and merge JSON schema references."
    )
    parser.add_argument("--debug", action="store_true", help="Enable debugging output")
    args = parser.parse_args()

    main(args.debug)
