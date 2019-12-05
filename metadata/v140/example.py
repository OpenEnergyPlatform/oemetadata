import json
import os

with open(os.path.join(os.path.dirname(__file__), "example.json"), "rb") as f:
    METADATA_V140_EXAMPLE = json.loads(f.read())
