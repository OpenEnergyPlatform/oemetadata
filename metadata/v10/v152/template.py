import json
import os

with open(os.path.join(os.path.dirname(__file__), "template.json"), "rb") as f:
    OEMETADATA_V152_TEMPLATE = json.loads(f.read())
