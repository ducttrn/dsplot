from ..node import Node


class GraphNode(Node):
    def __init__(self, val=0, neighbors=None):
        super().__init__(val)
        self.neighbors = neighbors if neighbors is not None else []
