from ..node import Node


class BinaryTreeNode(Node):
    def __init__(self, val=0, left=None, right=None):
        super().__init__(val)
        self.left = left
        self.right = right
