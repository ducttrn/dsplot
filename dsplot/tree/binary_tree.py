from queue import Queue
from typing import List, Literal, Union

import pygraphviz

from dsplot.config import config
from dsplot.errors import InputException

from .tree_node import BinaryTreeNode

Node = Union[int, str]


class BinaryTree:
    def __init__(self, nodes: List[Node]):
        if not nodes:
            raise InputException('Input list must have at least 1 element.')

        self.root = self.construct_tree(nodes)

    @staticmethod
    def construct_tree(nodes: List[Node]) -> BinaryTreeNode:
        nodes = iter(nodes)
        root = BinaryTreeNode(next(nodes))

        q = Queue()
        q.put(root)

        while True:
            cur_node = q.get()
            try:
                left_val = next(nodes)
                if left_val:
                    cur_node.left = BinaryTreeNode(left_val)
                    q.put(cur_node.left)

                right_val = next(nodes)
                if right_val:
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
        cur_id = 0
        q = Queue()
        q.put((self.root, cur_id))

        while not q.empty():
            node, node_id = q.get()
            graph.add_node(
                node_id,
                label=node.val,
                color=border_color,
                shape=shape,
                style=style,
                fillcolor=fill_color,
            )

            cur_id += 1
            graph.add_edge(node_id, cur_id)
            if node.left:
                q.put((node.left, cur_id))
            else:
                graph.add_node(
                    cur_id,
                    label=config.LEAF_LABEL,
                    color=border_color,
                    shape=config.LEAF_SHAPE,
                )

            cur_id += 1
            graph.add_edge(node_id, cur_id)
            if node.right:
                q.put((node.right, cur_id))
            else:
                graph.add_node(
                    cur_id,
                    label=config.LEAF_LABEL,
                    color=border_color,
                    shape=config.LEAF_SHAPE,
                )

    def preorder(self) -> List[Node]:
        return list(self._preorder(self.root))

    def _preorder(self, node):
        if node:
            yield node.val
            yield from self._preorder(node.left)
            yield from self._preorder(node.right)

    def inorder(self) -> List[Node]:
        return list(self._inorder(self.root))

    def _inorder(self, node):
        if node:
            yield from self._inorder(node.left)
            yield node.val
            yield from self._inorder(node.right)

    def postorder(self) -> List[Node]:
        return list(self._postorder(self.root))

    def _postorder(self, node):
        if node:
            yield from self._postorder(node.left)
            yield from self._postorder(node.right)
            yield node.val
