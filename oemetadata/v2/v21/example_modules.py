# SPDX-FileCopyrightText: 2026 Ludwig Hülk <@Ludee> © Reiner Lemoine Institut
# SPDX-FileCopyrightText: oemetadata <https://github.com/OpenEnergyPlatform/oemetadata/>
# SPDX-License-Identifier: MIT

import json
from pathlib import Path

from frictionless import Package


BASE_PATH = Path(__file__).parent

with open(BASE_PATH / "example_modules.json", "rb") as f:
    descriptor = json.load(f)

OEMETADATA_V21_EXAMPLE_MODULES = Package(descriptor, basepath=str(BASE_PATH))
