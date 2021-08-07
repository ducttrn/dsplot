import os

import pytest

from dsplot.tree import BinaryTree
from errors import InputException


def test_binary_tree():
    tree = BinaryTree(nodes=[5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1])

    assert tree.root.val == 5
    assert tree.root.right.left.val == 13
    assert tree.root.right.right.left.val == 5

    assert tree.preorder() == [5, 4, 11, 7, 2, 8, 13, 4, 5, 1]
    assert tree.inorder() == [7, 11, 2, 4, 5, 13, 8, 5, 4, 1]
    assert tree.postorder() == [7, 2, 11, 4, 13, 5, 1, 4, 8, 5]

    tree.plot('tests/test_data/tree.png')
    assert 'tree.png' in os.listdir('tests/test_data')

    with pytest.raises(InputException) as e:
        BinaryTree(nodes=[])
    assert str(e.value) == 'Input list must have at least 1 element.'
