"""create example from json schema
"""
import json
from pathlib import Path
from os.path import dirname


def main(schema_file_in: Path, example_file_out: Path) -> None:
    """
    Args:
        schema_file_in: path to schema file
        example_file_out: path to example file
    """
    with open(schema_file_in, "r", encoding="utf-8") as file:
        schema = json.load(file)

    example = generate_example(schema)

    with open(example_file_out, "w", encoding="utf-8") as file:
        json.dump(example, file, indent=4, ensure_ascii=False)


def generate_example(schema: dict) -> dict:
    """Recursively create example object from json schema object.
    Args:
        schema: json schema object
    Returns:
        dict: example object
    """

    schema = schema

    if schema.get("const"):
        return schema["const"]
    if schema.get("examples"):
        # the object has examples: return the first
        # TODO: maybe randomize?
        return schema["examples"][0]
    if schema["type"] == "object":
        result = {}
        for pname, prop in schema["properties"].items():
            ex = generate_example(prop)
            if ex:
                result[pname] = ex
        return result
    if schema["type"] == "array":
        # TODO: random number between minItems and maxItems?
        n = schema.get("minItems") or 1
        result = []
        for _ in range(n):
            ex = generate_example(schema["items"])
            if ex:
                result.append(ex)
        if result:
            return result


if __name__ == "__main__":
    pwd = dirname(__file__)
    main(pwd + "/demo_gen_schema.json", pwd + "/example.json")
