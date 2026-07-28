# SPDX-FileCopyrightText: 2026 Ludwig Hülk <@Ludee> © Reiner Lemoine Institut
# SPDX-FileCopyrightText: 2026 Jonas Huber <jh-RLI> © Reiner Lemoine Institut
# SPDX-FileCopyrightText: oemetadata <https://github.com/OpenEnergyPlatform/oemetadata/>
# SPDX-License-Identifier: MIT

from pathlib import Path


LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

BASE_PATH = Path("oemetadata/v2/")
VERSION = "v21"
VERSION_PATH = BASE_PATH / VERSION
SCHEMA_BUILD_PATH = VERSION_PATH / "build_source"
MAIN_SCHEMA_PATH = SCHEMA_BUILD_PATH / "schema_structure.json"
SCHEMA_REFS = SCHEMA_BUILD_PATH / "schemas"
SCHEMA_EXAMPLE_FIELDS = SCHEMA_BUILD_PATH / "scripts/example/fields.json"
SCHEMA_EXAMPLE_PROV = SCHEMA_BUILD_PATH / "scripts/example/contributors.json"
RESOLVED_SCHEMA_FILE_NAME = VERSION_PATH / "schema.json"
EXPECTED_SCHEMA_PATH = VERSION_PATH / "schema.json"
CONTEXT_PATH = VERSION_PATH / "context.json"

EXAMPLE_PATH = VERSION_PATH / "example.json"
EXAMPLE_MODULES_PATH = VERSION_PATH / "example_modules.json"
TEMPLATE_PATH = VERSION_PATH / "template.json"
GRAPH_PATH = VERSION_PATH / "graph.ttl"
LATEST_PATH = Path("oemetadata/latest/")
