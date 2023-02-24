import uuid
from queue import Queue
from typing import List, Literal, Union

import pygraphviz

from dsplot.config import config
from dsplot.errors import InputException
from dsplot.tree.tree_node import BinaryTreeNode

node_values = Union[int, str]


class BinaryTree:
    def __init__(self, nodes: List[node_values]):
        if not nodes:
            raise InputException('Input list must have at least 1 element.')

        self.root = self.construct_tree(nodes)

    @staticmethod
    def construct_tree(nodes: List[node_values]) -> BinaryTreeNode:
        nodes = iter(nodes)
        root = BinaryTreeNode(next(nodes))

        q = Queue()
        q.put(root)

        while True:
            cur_node = q.get()
            try:
                left_val = next(nodes)
                if left_val is not None:
                    cur_node.left = BinaryTreeNode(left_val)
                    q.put(cur_node.left)

                right_val = next(nodes)
                if right_val is not None:
                    cur_node.right = BinaryTreeNode(right_val)
                    q.put(cur_node.right)

            except StopIteration:
                break

        return root

    def plot(
        self,
        output_path: str = './tree.png',
        orientation: Literal['TB', 'LR'] = config.TREE_ORIENTATION,
        border_color: str = config.NODE_COLOR,
        shape: str = config.LEAF_SHAPE,
        style: str = config.NODE_STYLE,
        fill_color: str = config.NODE_FILL_COLOR,
    ):
        graph = pygraphviz.AGraph(directed=False)
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
        q = Queue()
        q.put(self.root)

        while not q.empty():
            node = q.get()
            graph.add_node(
                node.id,
                label=node.val,
                color=border_color,
                shape=shape,
                style=style,
                fillcolor=fill_color,
            )

            if node.left:
                graph.add_edge(node.id, node.left.id)
                q.put(node.left)
            else:
                self._add_leaf(graph, node, border_color)

            if node.right:
                graph.add_edge(node.id, node.right.id)
                q.put(node.right)
            else:
                self._add_leaf(graph, node, border_color)

    @staticmethod
    def _add_leaf(graph: pygraphviz.AGraph, node: BinaryTreeNode, border_color: str):
        # Generate random id for leaves
        leaf_id = uuid.uuid4()
        graph.add_edge(node.id, leaf_id)
        graph.add_node(
            leaf_id,
            label=config.LEAF_LABEL,
            color=border_color,
            shape=config.LEAF_SHAPE,
        )

    def preorder(self) -> List[node_values]:
        return list(self._preorder(self.root))

    def _preorder(self, node):
        if node:
            yield node.val
            yield from self._preorder(node.left)
            yield from self._preorder(node.right)

    def inorder(self) -> List[node_values]:
        return list(self._inorder(self.root))

    def _inorder(self, node):
        if node:
            yield from self._inorder(node.left)
            yield node.val
            yield from self._inorder(node.right)

    def postorder(self) -> List[node_values]:
        return list(self._postorder(self.root))

    def _postorder(self, node):
        if node:
            yield from self._postorder(node.left)
            yield from self._postorder(node.right)
            yield node.val
