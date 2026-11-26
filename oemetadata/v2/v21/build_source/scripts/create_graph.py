#!/usr/bin/env python3

# SPDX-FileCopyrightText: 2026 Philipp Schmurr <@CPPrentice> © Karlsruher Institut für Technologie
# SPDX-FileCopyrightText: 2026 Ludwig Hülk <@Ludee> © Reiner Lemoine Institut
# SPDX-FileCopyrightText: oemetadata <https://github.com/OpenEnergyPlatform/oemetadata/>
# SPDX-License-Identifier: MIT

"""Create JSON-LD and Turtle graphs from the OEMetadata examples.

Combines each example with the local context.json (instead of the remote
context referenced in the example) and writes:

* a JSON-LD file with inline context (e.g. for the JSON-LD Playground)
* the resulting RDF graph as Turtle

Run from the repository root.
"""

import json
import logging
import os
import subprocess
import sys
from pathlib import Path

from rdflib import Graph
from rdflib.compare import to_canonical_graph
from settings import (
    CONTEXT_PATH,
    EXAMPLE_MODULES_PATH,
    EXAMPLE_PATH,
    GRAPH_JSONLD_PATH,
    GRAPH_MODULE_JSONLD_PATH,
    GRAPH_MODULE_TTL_PATH,
    GRAPH_TTL_PATH,
    LOG_FORMAT,
)


ENCODING = "utf-8"

# Configuration
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)
logger = logging.getLogger(__name__)


def read_json(path: Path) -> dict:
    """Read a JSON file."""
    return json.loads(path.read_text(encoding=ENCODING))


def combine(example: dict, context: dict) -> dict:
    """Replace the remote @context of the example with the local context."""
    return {
        "@context": context["@context"],
        **{key: value for key, value in example.items() if key != "@context"},
    }


def create_graph(
    example_path: Path, context: dict, jsonld_path: Path, ttl_path: Path
) -> None:
    """Write the combined JSON-LD file and the resulting Turtle graph."""
    combined = combine(read_json(example_path), context)

    jsonld_path.write_text(
        json.dumps(combined, indent=2, ensure_ascii=False) + "\n",
        encoding=ENCODING,
    )

    graph = Graph()
    graph.parse(data=json.dumps(combined), format="json-ld")
    # Canonical blank node labels make the Turtle output reproducible,
    # so regenerating the files only produces a diff if the graph changed.
    graph = to_canonical_graph(graph)
    graph.serialize(destination=ttl_path, format="longturtle", encoding=ENCODING)

    logger.info(
        "%s: %d triples -> %s, %s",
        example_path.name,
        len(graph),
        jsonld_path.name,
        ttl_path.name,
    )


if __name__ == "__main__":
    if os.environ.get("PYTHONHASHSEED") != "0":
        # subprocess instead of os.exec* to behave the same on Windows
        sys.exit(
            subprocess.run(
                [sys.executable, *sys.argv],
                env={**os.environ, "PYTHONHASHSEED": "0"},
            ).returncode
        )

    logger.info("Create OEMetadata Graph from Example and Example Modules.")

    context = read_json(CONTEXT_PATH)

    create_graph(EXAMPLE_PATH, context, GRAPH_JSONLD_PATH, GRAPH_TTL_PATH)
    create_graph(
        EXAMPLE_MODULES_PATH, context, GRAPH_MODULE_JSONLD_PATH, GRAPH_MODULE_TTL_PATH
    )

    logger.info("OEMetadata Graph created!")
