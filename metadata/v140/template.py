import json
import os

with open(os.path.join(os.path.dirname(__file__), "template.json"), "r") as f:
    METADATA_V140_TEMPLATE = json.loads(f.read())
