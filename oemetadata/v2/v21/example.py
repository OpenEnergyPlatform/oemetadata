# SPDX-FileCopyrightText: 2024 Ludwig Hülk <@Ludee> © Reiner Lemoine Institut
# SPDX-FileCopyrightText: 2024 Jonas Huber <jh-RLI> © Reiner Lemoine Institut
# SPDX-FileCopyrightText: oemetadata <https://github.com/OpenEnergyPlatform/oemetadata/>
# SPDX-License-Identifier: MIT

import json
from pathlib import Path

from frictionless import Package


BASE_PATH = Path(__file__).parent

with open(BASE_PATH / "example.json", "rb") as f:
    descriptor = json.load(f)

OEMETADATA_V21_EXAMPLE = Package(descriptor, basepath=str(BASE_PATH))
