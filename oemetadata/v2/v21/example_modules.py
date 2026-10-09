# SPDX-FileCopyrightText: 2026 Ludwig Hülk <@Ludee> © Reiner Lemoine Institut
# SPDX-FileCopyrightText: oemetadata <https://github.com/OpenEnergyPlatform/oemetadata/>
# SPDX-License-Identifier: MIT

import json
from pathlib import Path

from frictionless import FrictionlessException, Package


BASE_PATH = Path(__file__).parent

with open(BASE_PATH / "example_modules.json", "rb") as f:
    descriptor = json.load(f)

OEMETADATA_V21_EXAMPLE_MODULES = descriptor
OEMETADATA_V21_EXAMPLE_MODULES_DATAPACKAGE: Package | None = None
try:
    OEMETADATA_V21_EXAMPLE_MODULES_DATAPACKAGE = Package.from_descriptor(descriptor)
except FrictionlessException:
    pass  # This is tested in the OEMetadata tests and should therefore fail the deployment pipeline for a release
    # The tests need this file to run so we just fail silently if the data package can not be constructed
