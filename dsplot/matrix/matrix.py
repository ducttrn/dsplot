from typing import List, Literal, Union

import pygraphviz

from dsplot.config import config
from dsplot.errors import InputException
from dsplot.matrix.matrix_node import MatrixNode

node_values = Union[int, str]


class Matrix:
    def __init__(self, nodes: List[List[node_values]]):
        if not nodes or not nodes[0]:
            raise InputException('Input list must have at least 1 element.')

        self.nodes = self.construct_matrix(nodes)

    @staticmethod
    def construct_matrix(nodes: List[List[node_values]]) -> List[List[MatrixNode]]:
        for i in range(len(nodes)):
            for j in range(len(nodes[0])):
                nodes[i][j] = MatrixNode(nodes[i][j])

        return nodes

    def plot(
        self,
        output_path='./matrix.png',
        orientation: Literal['TB', 'LR'] = config.MATRIX_ORIENTATION,
        border_color: str = config.BOX_COLOR,
        shape: str = config.BOX_SHAPE,
        style: str = config.BOX_STYLE,
        fill_color: str = config.BOX_FILL_COLOR,
    ):
        graph = pygraphviz.AGraph(ranksep=config.RANK_SEP)
        graph.graph_attr['rankdir'] = orientation
        graph.graph_attr['ordering'] = 'out'

        self._add_nodes(graph, border_color, shape, style, fill_color)
        graph.layout(prog='dot')
        graph.draw(output_path)
        graph.close()

    def _add_nodes(
        self,
        graph: pygraphviz.AGraph,
        border_color: str,
        shape: str,
        style: str,
        fill_color: str,
    ):

        node_ids = []
        for row in self.nodes:
            row_ids = []
            for node in row:
                graph.add_node(
                    node.id,
                    label=node.val,
                    color=border_color,
                    shape=shape,
                    style=style,
                    fillcolor=fill_color,
                )
                row_ids.append(node.id)

            graph.add_subgraph(row_ids, rank=config.RANK)
            node_ids.append(row_ids)

        for i in range(1, len(node_ids)):
            graph.add_edge(node_ids[i - 1][0], node_ids[i][0], style=config.EDGE_STYLE)
