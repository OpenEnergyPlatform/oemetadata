# SPDX-FileCopyrightText: Ludwig Hülk <@Ludee> © Reiner Lemoine Institut
# SPDX-FileCopyrightText: Jonas Huber <jh-RLI> © Reiner Lemoine Institut
#
# SPDX-License-Identifier: MIT

import json
import os

with open(os.path.join(os.path.dirname(__file__), "example.json"), "rb") as f:
    OEMETADATA_LATEST_EXAMPLE = json.loads(f.read())
