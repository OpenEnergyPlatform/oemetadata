# SPDX-FileCopyrightText: 2026 Philipp Schmurr <@CPPrentice> © Karlsruher Institut für Technologie
# SPDX-FileCopyrightText: oemetadata <https://github.com/OpenEnergyPlatform/oemetadata/>
# SPDX-License-Identifier: MIT

import collections
import pytest
import rdflib
from pyld import jsonld


# we should not use this one as the online resolution targets the latest context instead of the one of this release
@pytest.fixture
def example() -> rdflib.Graph:
    from oemetadata.v2.v21.example import OEMETADATA_V21_EXAMPLE
    descriptor = OEMETADATA_V21_EXAMPLE
    graph = rdflib.Graph()
    graph.parse(data=descriptor, format='json-ld')
    return graph

@pytest.fixture
def json_example_local_context() -> dict:
    from oemetadata.v2.v21.example import OEMETADATA_V21_EXAMPLE
    from oemetadata.v2.v21.context import OEMETADATA_V21_CONTEXT

    jsonld = {**OEMETADATA_V21_EXAMPLE}

    # Inject local context
    jsonld.update(OEMETADATA_V21_CONTEXT)
    return jsonld


@pytest.fixture
def local_context_example() -> rdflib.Graph:
    from oemetadata.v2.v21.graph import OEMETADATA_V21_GRAPH
    return OEMETADATA_V21_GRAPH

def stringify(x, nms) -> str:
    try:
        return nms.curie(x)
    except ValueError:
        return str(x)


def test_duplicate_literals(local_context_example):
    nsm = local_context_example.namespace_manager
    object_per_sp = collections.defaultdict(list)
    for (s, p, o) in local_context_example:
        object_per_sp[(s, p)].append(o)

    ns_lookup = dict(nsm.namespaces())
    multiple_value_predicate_whitelist = {
        ns_lookup['dct'] + 'contributor',
        ns_lookup['sc'] + 'author',
        ns_lookup['dcat'] + 'keyword',
        ns_lookup['dct'] + 'license',
        ns_lookup['prov'] + 'value',
        ns_lookup['dct'] + 'language',
    }

    multiple_objects = []
    for (s, p), object_list in object_per_sp.items():
        if len(object_list) > 1 and p not in multiple_value_predicate_whitelist:
            multiple_objects.append(((s, p), object_list))
            print(stringify(s, nsm), stringify(p, nsm), [str(x) for x in object_list])
    assert len(multiple_objects) == 0


def test_create_local_turtle(local_context_example):
    local_context_example.serialize(destination='graph.ttl', format='turtle')
    

def test_pyld(json_example_local_context):
    expanded = jsonld.expand(json_example_local_context)
    


