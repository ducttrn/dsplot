import random
from queue import Queue
from typing import List, Optional

import pygraphviz

from tree import TreeNode


class BinaryTree:
    def __init__(self, nodes: List[Optional[int]]):
        if not nodes:
            raise Exception

        self.nodes = nodes
        self.root = self.construct_tree(nodes)

    @staticmethod
    def construct_tree(nodes: List[Optional[int]]) -> TreeNode:
        nodes = iter(nodes)
        root = TreeNode(next(nodes))

        q = Queue()
        q.put(root)

        while True:
            cur_node = q.get()
            try:
                left_val = next(nodes)
                if left_val:
                    cur_node.left = TreeNode(left_val)
                    q.put(cur_node.left)

                right_val = next(nodes)
                if right_val:
                    cur_node.right = TreeNode(right_val)
                    q.put(cur_node.right)

            except StopIteration:
                break

        return root

    def preorder(self) -> List[int]:
        return list(self._preorder(self.root))

    def _preorder(self, node):
        if node:
            yield node.val
            yield from self._preorder(node.left)
            yield from self._preorder(node.right)

    def inorder(self) -> List[int]:
        return list(self._inorder(self.root))

    def _inorder(self, node):
        if node:
            yield from self._inorder(node.left)
            yield node.val
            yield from self._inorder(node.right)

    def postorder(self) -> List[int]:
        return list(self._postorder(self.root))

    def _postorder(self, node):
        if node:
            yield from self._postorder(node.left)
            yield from self._postorder(node.right)
            yield node.val

    def plot(self):
        graph = pygraphviz.AGraph(directed=True)
        graph.graph_attr["rankdir"] = "TB"

        self._add_nodes(graph, self.root)
        graph.layout(prog='dot')
        graph.draw('foo.png')
        graph.close()

    @staticmethod
    def _add_nodes(graph: pygraphviz.AGraph, node: TreeNode):
        cur_id = 0
        level = 0

        q = Queue()
        q.put((node, cur_id, level))
        levels = []

        while not q.empty():
            node, node_id, level = q.get()
            graph.add_node(node_id, label=node.val, color='black')
            if len(levels) == level:
                levels.append([node_id])
            else:
                levels[level].append(node_id)

            if node.left:
                cur_id += 1
                q.put((node.left, cur_id, level + 1))
                graph.add_edge(node_id, cur_id)

            if node.right:
                cur_id += 1
                q.put((node.right, cur_id, level + 1))
                graph.add_edge(node_id, cur_id)


if __name__ == "__main__":
    tree = BinaryTree(nodes=[5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1, 23, 12])
    tree.plot()
