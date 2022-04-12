import os

import pytest

from dsplot.errors import InputException
from dsplot.matrix import Matrix


def test_matrix():
    matrix = Matrix([[1, 2, 3], [4, 5, 6], [1, 2, 6]])

    matrix.plot('tests/test_data/matrix.png', fill_color='#aec6cf')
    assert 'matrix.png' in os.listdir('tests/test_data')

    with pytest.raises(InputException) as e:
        Matrix(nodes=[[]])
    assert str(e.value) == 'Input list must have at least 1 element.'
