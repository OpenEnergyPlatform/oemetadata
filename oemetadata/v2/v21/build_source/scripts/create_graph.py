#!/usr/bin/env python3

# SPDX-FileCopyrightText: 2026 Philipp Schmurr <@CPPrentice> © Karlsruher Institut für Technologie
# SPDX-FileCopyrightText: oemetadata <https://github.com/OpenEnergyPlatform/oemetadata/>
# SPDX-License-Identifier: MIT

import json
import logging

from rdflib import Graph


from settings import (
    CONTEXT_PATH,
    EXAMPLE_PATH,
    GRAPH_PATH,
    LOG_FORMAT
)


# Configuration
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)
logger = logging.getLogger(__name__)


if __name__ == '__main__':
    logger.info("Create OEMetadata Graph from Example.")
    graph = Graph()
    jsonld = json.loads(EXAMPLE_PATH.read_text())
    context = json.loads(CONTEXT_PATH.read_text())

    # Inject local context
    jsonld['@context'] = context
    
    graph.parse(data=jsonld, format='json-ld')
    graph.serialize(destination=GRAPH_PATH, format='longturtle')
    logger.info("OEMetadata Graph created!")
