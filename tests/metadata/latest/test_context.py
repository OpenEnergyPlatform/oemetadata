# SPDX-FileCopyrightText: Jonas Huber <jh-RLI> © Reiner Lemoine Institut
#
# SPDX-License-Identifier: MIT

import pytest
from pyld import jsonld
import json
import os


@pytest.fixture
def load_files():
    """Load the example.json and context.json files."""
    base_path = "metadata/latest/"
    example_file = os.path.join(base_path, "example.json")
    context_file = os.path.join(base_path, "context.json")

    # Load example.json
    with open(example_file, "r") as ef:
        example_data = json.load(ef)

    # Load context.json
    with open(context_file, "r") as cf:
        context_data = json.load(cf)

    return example_data, context_data


def clean_context(context):
    """Remove invalid entries (placeholders or invalid @type)."""
    cleaned_context = {}
    for key, value in context.items():
        if isinstance(value, dict):
            # Remove entries with invalid @id or @type
            if value.get("@id") == "xx" or value.get("@type") == "xx":
                continue
            # Keep only valid entries
            cleaned_context[key] = {
                k: v
                for k, v in value.items()
                if v != "xx" and (k != "@type" or is_valid_type(v))
            }
        elif value != "xx":
            cleaned_context[key] = value
    return cleaned_context


def is_valid_type(value):
    """Check if @type value is a valid absolute or compact IRI."""
    # Valid if it's a known compact IRI (e.g., xsd:string)
    if ":" in value and not value.startswith("@"):
        return True
    # Invalid if it contains spaces or invalid characters
    return False


def clean_null_ids(data):
    """Recursively remove @id entries with null values."""
    if isinstance(data, dict):
        return {
            key: clean_null_ids(value)
            for key, value in data.items()
            if not (key == "@id" and value is None)
        }
    elif isinstance(data, list):
        return [clean_null_ids(item) for item in data]
    return data


def test_jsonld_combination(load_files):
    """Test combining example.json with context.json and validating JSON-LD."""
    # try:
    # Get the example and context data
    example_data, context_data = load_files

    # Clean the @context from placeholders and invalid entries
    cleaned_context = clean_context(context_data["@context"])

    # Update the @context for each resource in the resources array
    for resource in example_data.get("resources", []):
        resource["@context"] = cleaned_context

    # Remove @id with null values from resources
    cleaned_example_data = clean_null_ids(example_data)

    # Validate each resource as JSON-LD
    for resource in cleaned_example_data["resources"]:
        expanded = jsonld.expand(resource)
        assert (
            expanded
        ), f"Validation failed for resource: {resource.get('@id', 'unknown')}"
