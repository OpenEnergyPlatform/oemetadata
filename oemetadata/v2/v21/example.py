# SPDX-FileCopyrightText: 2024 Ludwig Hülk <@Ludee> © Reiner Lemoine Institut
# SPDX-FileCopyrightText: 2024 Jonas Huber <jh-RLI> © Reiner Lemoine Institut
# SPDX-FileCopyrightText: oemetadata <https://github.com/OpenEnergyPlatform/oemetadata/>
# SPDX-License-Identifier: MIT

import json
import os

from frictionless import Package


BASE_PATH = os.path.dirname(__file__)

with open(os.path.join(BASE_PATH, "example.json"), encoding="utf-8") as f:
    descriptor = json.load(f)

OEMETADATA_V21_EXAMPLE = Package(descriptor, basepath=BASE_PATH)
