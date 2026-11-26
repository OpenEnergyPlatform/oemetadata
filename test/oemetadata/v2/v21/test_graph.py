# SPDX-FileCopyrightText: 2026 Ludwig Hülk <@Ludee> © Reiner Lemoine Institut
# SPDX-FileCopyrightText: oemetadata <https://github.com/OpenEnergyPlatform/oemetadata/>
# SPDX-License-Identifier: MIT

"""Semantic tests for the OEMetadata v2.1 context and example graphs.

The examples are combined with the local context.json, because the @context
in the examples points to the latest release and not to this version.
The combined files and graphs are created by build_source/scripts/create_graph.py.
"""

import collections
import json
from pathlib import Path

import pytest
from pyld import jsonld
from rdflib import Graph, Literal, URIRef
from rdflib.compare import isomorphic
from rdflib.namespace import XSD

from oemetadata.v2.v21.context import OEMETADATA_V21_CONTEXT
from oemetadata.v2.v21.example import OEMETADATA_V21_EXAMPLE
from oemetadata.v2.v21.example_modules import OEMETADATA_V21_EXAMPLE_MODULES
from oemetadata.v2.v21.graph.example_graph import (
    OEMETADATA_V21_EXAMPLE_GRAPH_TTL,
)
from oemetadata.v2.v21.graph.example_graph_module import (
    OEMETADATA_V21_EXAMPLE_GRAPH_MODULE_TTL,
)


VERSION_PATH = Path("oemetadata/v2/v21")

CASES = {
    "example": (
        OEMETADATA_V21_EXAMPLE,
        VERSION_PATH / "example_graph.jsonld",
        OEMETADATA_V21_EXAMPLE_GRAPH_TTL,
    ),
    "example_modules": (
        OEMETADATA_V21_EXAMPLE_MODULES,
        VERSION_PATH / "example_graph_module.jsonld",
        OEMETADATA_V21_EXAMPLE_GRAPH_MODULE_TTL,
    ),
}


def combine(example: dict) -> dict:
    """Replace the remote @context of the example with the local context."""
    return {
        "@context": OEMETADATA_V21_CONTEXT["@context"],
        **{key: value for key, value in example.items() if key != "@context"},
    }


def via_turtle(graph: Graph) -> Graph:
    """Round-trip through Turtle to get the same literal forms as the stored files."""
    return Graph().parse(data=graph.serialize(format="longturtle"), format="turtle")


def without_xsd_string(graph: Graph) -> Graph:
    """Drop explicit ^^xsd:string, which is equivalent to a plain literal in RDF 1.1."""
    result = Graph()
    for s, p, o in graph:
        if isinstance(o, Literal) and o.datatype == XSD.string:
            o = Literal(str(o))
        result.add((s, p, o))
    return result


def set_predicates(context: dict) -> set:
    """IRIs of all terms with "@container": "@set", i.e. keys that hold arrays."""
    prefixes = {
        k: v for k, v in context.items() if isinstance(v, str) and v.startswith("http")
    }

    def expand(curie: str) -> str:
        prefix, _, local = curie.partition(":")
        return prefixes.get(prefix, prefix + ":") + local

    found = set()

    def walk(ctx: dict) -> None:
        for definition in ctx.values():
            if not isinstance(definition, dict):
                continue
            iri = definition.get("@id") or definition.get("@reverse")
            if definition.get("@container") == "@set" and iri:
                found.add(URIRef(expand(iri)))
            walk(definition.get("@context", {}))

    walk(context)
    return found


@pytest.mark.parametrize("case", CASES)
def test_jsonld_is_up_to_date(case):
    example, jsonld_path, _ = CASES[case]
    stored = json.loads(jsonld_path.read_text(encoding="utf-8"))
    assert stored == combine(
        example
    ), f"{jsonld_path.name} is outdated, run create_graph.py"


@pytest.mark.parametrize("case", CASES)
def test_graph_is_up_to_date(case):
    example, _, stored = CASES[case]
    fresh = Graph().parse(data=json.dumps(combine(example)), format="json-ld")
    assert isomorphic(
        via_turtle(fresh), stored
    ), "Turtle graph is outdated, run create_graph.py"


@pytest.mark.parametrize("case", CASES)
def test_pyld_and_rdflib_agree(case):
    example, _, _ = CASES[case]
    combined = combine(example)
    nquads = jsonld.to_rdf(combined, {"format": "application/n-quads"})
    graph_pyld = Graph().parse(data=nquads, format="nquads")
    graph_rdflib = Graph().parse(data=json.dumps(combined), format="json-ld")
    assert len(graph_pyld) > 0
    assert isomorphic(without_xsd_string(graph_pyld), without_xsd_string(graph_rdflib))


@pytest.mark.parametrize("case", CASES)
def test_multiple_values_only_for_arrays(case):
    """A subject may have several values for a predicate only if the key is an array."""
    _, _, graph = CASES[case]
    allowed = set_predicates(OEMETADATA_V21_CONTEXT["@context"])
    nsm = graph.namespace_manager

    objects = collections.defaultdict(list)
    for s, p, o in graph:
        objects[(s, p)].append(o)

    unexpected = [
        f"{s.n3(nsm)} {p.n3(nsm)} {[str(o) for o in values]}"
        for (s, p), values in objects.items()
        if len(values) > 1 and p not in allowed
    ]
    assert not unexpected, "\n".join(unexpected)
