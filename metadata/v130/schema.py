import json
import os

with open(os.path.join(os.path.dirname(__file__), "schema.json"), "r") as f:
    METADATA_V130_SCHEMA = json.loads(f.read())
