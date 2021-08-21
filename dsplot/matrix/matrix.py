from typing import List, Union

import pygraphviz

from dsplot.config import config
from dsplot.errors import InputException

Node = Union[int, str]


class Matrix:
    def __init__(self, nodes: List[List[Node]]):
        if not nodes or not nodes[0]:
            raise InputException('Input list must have at least 1 element.')

        self.nodes = nodes

    def plot(self, output_path='./matrix.png'):
        graph = pygraphviz.AGraph(ranksep=config.RANK_SEP)
        graph.graph_attr['rankdir'] = 'TB'
        graph.graph_attr['ordering'] = 'out'

        self._add_nodes(graph)
        graph.layout(prog='dot')
        graph.draw(output_path)
        graph.close()

    def _add_nodes(self, graph):
        node_id = 0
        node_ids = []
        for row in self.nodes:
            row_ids = []
            for node in row:
                graph.add_node(
                    node_id,
                    label=node,
                    color=config.BOX_COLOR,
                    shape=config.BOX_SHAPE,
                    style=config.BOX_STYLE,
                    fillcolor=config.BOX_FILL_COLOR,
                )
                row_ids.append(node_id)
                node_id += 1

            graph.add_subgraph(row_ids, rank=config.RANK)
            node_ids.append(row_ids)

        for i in range(1, len(node_ids)):
            graph.add_edge(node_ids[i - 1][0], node_ids[i][0], style=config.EDGE_STYLE)
