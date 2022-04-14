import uuid


class Node:
    def __init__(self, val):
        self.val = val
        self.id = uuid.uuid4()
