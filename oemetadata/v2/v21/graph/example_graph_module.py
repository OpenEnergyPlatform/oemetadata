# SPDX-FileCopyrightText: 2026 Philipp Schmurr <@CPPrentice> © Karlsruher Institut für Technologie
# SPDX-FileCopyrightText: 2026 Ludwig Hülk <@Ludee> © Reiner Lemoine Institut
# SPDX-FileCopyrightText: oemetadata <https://github.com/OpenEnergyPlatform/oemetadata/>
# SPDX-License-Identifier: MIT

from pathlib import Path

from rdflib import Graph


BASE_PATH = Path(__file__).parent

OEMETADATA_V21_EXAMPLE_GRAPH_MODULE_TTL = Graph()
OEMETADATA_V21_EXAMPLE_GRAPH_MODULE_TTL.parse(
    source=BASE_PATH / "example_graph_module.ttl", format="turtle"
)

OEMETADATA_V21_EXAMPLE_GRAPH_MODULE_JSONLD = Graph()
OEMETADATA_V21_EXAMPLE_GRAPH_MODULE_JSONLD.parse(
    source=BASE_PATH / "example_graph_module.jsonld", format="json-ld"
)
