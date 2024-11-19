# SPDX-FileCopyrightText: Ludwig Hülk <@Ludee> © Reiner Lemoine Institut
# SPDX-FileCopyrightText: Jonas Huber <jh-RLI> © Reiner Lemoine Institut
#
# SPDX-License-Identifier: MIT

from pathlib import Path

LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

BASE_PATH = Path("metadata/v2/")
VERSION = "v20"
VERSION_PATH = BASE_PATH / VERSION
SCHEMA_BUILD_PATH = VERSION_PATH / "build_source"
MAIN_SCHEMA_PATH = SCHEMA_BUILD_PATH / "schema_structure.json"
SCHEMA_REFS = SCHEMA_BUILD_PATH / "schemas"
SCHEMA_EXAMPLE_FIELDS = SCHEMA_BUILD_PATH / "scripts/example_fields.json"
SCHEMA_EXAMPLE_PROV = SCHEMA_BUILD_PATH / "scripts/example_contributors.json"
RESOLVED_SCHEMA_FILE_NAME = VERSION_PATH / "schema.json"
EXPECTED_SCHEMA_PATH = VERSION_PATH / "schema.json"

EXAMPLE_PATH = VERSION_PATH / "example.json"

TEMPLATE_PATH = VERSION_PATH / "template.json"
