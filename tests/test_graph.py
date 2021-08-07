import os

import pytest

from dsplot.errors import InputException
from dsplot.graph import Graph


def test_graph():
    graph = Graph(
        {0: [1, 4, 5], 1: [3, 4], 2: [1], 3: [2, 4], 4: [], 5: []}, directed=True
    )

    assert graph.bfs() == [0, 1, 4, 5, 3, 2]
    assert graph.dfs() == [0, 1, 3, 2, 4, 5]

    graph.plot('tests/test_data/graph.png')
    assert 'graph.png' in os.listdir('tests/test_data')

    with pytest.raises(InputException) as e:
        Graph({})
    assert str(e.value) == 'Input list must have at least 1 element.'
