import pathlib

from rdflib import Graph


BASE_PATH = pathlib.Path(__file__).parent
OEMETADATA_V21_GRAPH = Graph()
OEMETADATA_V21_GRAPH.parse(source=BASE_PATH / 'graph.ttl', format='turtle')
