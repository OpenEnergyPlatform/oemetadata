# SPDX-FileCopyrightText: 2026 Philipp Schmurr <@CPPrentice> © Karlsruher Institut für Technologie
# SPDX-FileCopyrightText: oemetadata <https://github.com/OpenEnergyPlatform/oemetadata/>
# SPDX-License-Identifier: MIT

import json
import pathlib


BASE_PATH = pathlib.Path(__file__).parent
with open(BASE_PATH / "context.json", "rb") as f:
    OEMETADATA_V21_CONTEXT = json.loads(f.read())
