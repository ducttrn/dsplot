from queue import Queue
from typing import Dict, List, Literal, Union

import pygraphviz

from dsplot.config import config
from dsplot.errors import InputException
from dsplot.graph.graph_node import GraphNode

node_values = Union[int, str]
edge_values = Union[int, str]


class Graph:
    def __init__(
        self,
        nodes: Dict[node_values, List[node_values]],
        directed: bool = False,
        edges: Dict[edge_values, edge_values] = None,
    ):
        if not nodes:
            raise InputException('Input list must have at least 1 element.')

        self.directed = directed
        self.nodes = self.construct_graph(nodes)
        self.edges = edges or {}

    @staticmethod
    def construct_graph(nodes: Dict[node_values, List[node_values]]) -> List[GraphNode]:
        node_map = {}
        for node_val in nodes:
            node = GraphNode(node_val)
            node_map[node_val] = node

        for node_val in nodes:
            node = node_map[node_val]
            for neighbor in nodes[node_val]:
                node.neighbors.append(node_map[neighbor])

        return list(node_map.values())

    def plot(
        self,
        output_path='./graph.png',
        orientation: Literal['TB', 'LR'] = config.GRAPH_ORIENTATION,
        border_color: str = config.NODE_COLOR,
        shape: str = config.NODE_SHAPE,
        style: str = config.NODE_STYLE,
        fill_color: str = config.NODE_FILL_COLOR,
    ):
        graph = pygraphviz.AGraph(directed=self.directed)
        graph.graph_attr['rankdir'] = orientation

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
        for node in self.nodes:
            graph.add_node(
                node.id,
                label=node.val,
                color=border_color,
                shape=shape,
                style=style,
                fillcolor=fill_color,
            )
            for neighbor in node.neighbors:
                edge_weight = self.edges.get(
                    f'{node.val}{neighbor.val}'
                ) or self.edges.get(f'{neighbor.val}{node.val}')
                graph.add_edge(node.id, neighbor.id, label=edge_weight or '')

    def dfs(self) -> List[node_values]:
        dfs_nodes = []
        visited = set()

        def _dfs(cur_node):
            dfs_nodes.append(cur_node.val)
            visited.add(cur_node)
            for neighbor in cur_node.neighbors:
                if neighbor not in visited:
                    _dfs(neighbor)

        _dfs(self.nodes[0])
        return dfs_nodes

    def bfs(self) -> List[node_values]:
        bfs_nodes = []

        q = Queue()
        q.put(self.nodes[0])
        visited = set()
        visited.add(self.nodes[0])

        while not q.empty():
            node = q.get()
            bfs_nodes.append(node.val)

            for neighbor in node.neighbors:
                if neighbor not in visited:
                    q.put(neighbor)
                    visited.add(neighbor)

        return bfs_nodes
