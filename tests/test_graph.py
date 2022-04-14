import os

import pytest

from dsplot.errors import InputException
from dsplot.graph import Graph


def test_graph():
    graph = Graph(
        {0: [1, 4, 5], 1: [3, 4], 2: [1], 3: [2, 4], 4: [], 5: []},
        directed=True,
        edges={'01': 1, '04': 4, '05': 5, '13': 3, '14': 4, '21': 2, '32': 3, '34': 4},
    )

    assert graph.bfs() == [0, 1, 4, 5, 3, 2]
    assert graph.dfs() == [0, 1, 3, 2, 4, 5]

    graph.plot('tests/test_data/directed_graph.png', fill_color='#aec6cf')
    assert 'directed_graph.png' in os.listdir('tests/test_data')

    graph = Graph(
        {
            'A': ['B', 'D'],
            'B': ['A', 'C'],
            'C': ['B', 'D', 'E'],
            'D': ['A', 'C'],
            'E': ['C', 'F', 'G'],
            'F': ['E'],
            'G': ['E'],
        },
        directed=False,
        edges={'AD': 4, 'AB': 2, 'BC': 3, 'CD': 4, 'CE': 5, 'EF': 6, 'EG': 7},
    )
    graph.plot('tests/test_data/undirected_graph.png', fill_color='#aec6cf')
    assert 'undirected_graph.png' in os.listdir('tests/test_data')

    with pytest.raises(InputException) as e:
        Graph({})
    assert str(e.value) == 'Input list must have at least 1 element.'
