import json
import os

with open(os.path.join(os.path.dirname(__file__), "schema.json"), "rb") as f:
    OEMETADATA_V141_SCHEMA = json.loads(f.read())
