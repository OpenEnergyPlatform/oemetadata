# SPDX-FileCopyrightText: 2026 Philipp Schmurr <@CPPrentice> © Karlsruher Institut für Technologie
# SPDX-FileCopyrightText: oemetadata <https://github.com/OpenEnergyPlatform/oemetadata/>
# SPDX-License-Identifier: MIT

import pathlib

from rdflib import Graph


BASE_PATH = pathlib.Path(__file__).parent
OEMETADATA_V21_GRAPH = Graph()
OEMETADATA_V21_GRAPH.parse(source=BASE_PATH / 'graph.ttl', format='turtle')
