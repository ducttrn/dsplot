<p align="center">
  <img src="https://github.com/billtrn/dsplot/blob/master/img/logo.png?raw=true" alt="dsplot-logo">
</p>

<h1 align="center">
DSPlot - Data Structure Visualization
</h1>

<p align="center">
  <a href="https://badge.fury.io/py/dsplot">
    <img src="https://badge.fury.io/py/dsplot.svg" alt="PyPI version" height="18">
  </a>
  <a href="https://dl.circleci.com/status-badge/redirect/circleci/5AFmWEafY2avg6nRh9G3Rw/7QZG8vWJDWRJPjULgXxNSc/tree/master">
    <img src="https://dl.circleci.com/status-badge/img/circleci/5AFmWEafY2avg6nRh9G3Rw/7QZG8vWJDWRJPjULgXxNSc/tree/master.svg?style=svg&circle-token=5155d812aff1e1b13de2a0313ba1a3e6c600fa85" alt="Build Status" height="18">
  </a>
  <a href="https://coveralls.io/github/billtrn/dsplot?branch=master">
    <img src="https://coveralls.io/repos/github/billtrn/dsplot/badge.svg?branch=master" alt="Coverage Status" height="18">
  </a>
  <a href="https://github.com/billtrn/dsplot/blob/master/LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License" height="18">
  </a>

<hr />

<p align="center">
  Graph Pythonically. 📏📐🖍️🐍
</p>

DSPlot is a tool to simply visualize tree and graph data structures by serving as a Pythonic interface to the [Graphviz](https://graphviz.org/) layout.
DSPlot allows you to easily draw trees, graphs (both directed and undirected), and matrices by passing data in primitive form and directly output an image.


## 📖 Table of Contents
- [⬇ Installation](#-installation)
- [📦 Features](#-features)
- [🎁 Bonus](#-bonus)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
## ⬇ Installation

#### 0. Prerequisites
- Python 3.9 or later
- `pip`
- `virtualenv`

#### 1. Install Graphviz
- MacOS:
```
brew install graphviz
```
- Linux:
```
apt-get install graphviz libgraphviz-dev
```
- Other OS(s): https://graphviz.org/download/

#### 2. Install package
```
$ pip install dsplot
```

## 📦 Features
- Binary Tree:
```python
from dsplot.tree import BinaryTree

tree = BinaryTree(nodes=[5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1])
tree.plot()
```
<p align="center">
  <img src="https://github.com/billtrn/dsplot/blob/master/img/tree.png?raw=true" alt="tree" width="400">
</p>

- Graph:
```python
from dsplot.graph import Graph

graph = Graph(
    {0: [1, 4, 5], 1: [3, 4], 2: [1], 3: [2, 4], 4: [], 5: []}, directed=True
)
graph.plot()
```
<p align="center">
  <img src="https://github.com/billtrn/dsplot/blob/master/img/directed.png?raw=true" alt="directed" width="300">
</p>

```python
from dsplot.graph import Graph

graph = Graph(
    {1: [2, 4], 2: [1, 3], 3: [2, 4, 5], 4: [1, 3], 5: [3, 6, 7], 6: [5], 7: [5]}, directed=False
)
graph.plot()
```
<p align="center">
  <img src="https://github.com/billtrn/dsplot/blob/master/img/undirected.png?raw=true" alt="undirected" width="400">
</p>

- Matrix:
```python
from dsplot.matrix import Matrix

matrix = Matrix([[1, 2, 3], [4, 5, 6], [1, 2, 6]])
matrix.plot()
```
<p align="center">
  <img src="https://github.com/billtrn/dsplot/blob/master/img/matrix.png?raw=true" alt="matrix" width="200">
</p>

- Customization: <br>
You can customize the border color, shape, style, and fill color of the nodes, and the orientation (left to right - LR, top to bottom - TB) of the graph.
```python
from dsplot.graph import Graph

graph = Graph(
    {0: [1, 4, 5], 1: [3, 4], 2: [1], 3: [2, 4], 4: [], 5: []}, directed=True
)
graph.plot(fill_color='#aec6cf')
```
<p align="center">
  <img src="https://github.com/billtrn/dsplot/blob/master/img/color_graph.png?raw=true" alt="color_graph" width="300">
</p>

```python
from dsplot.tree import BinaryTree

tree = BinaryTree(nodes=[5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1])
tree.plot(orientation='LR', border_color='#FFCE30', fill_color='#aec6cf')
```
<p align="center">
  <img src="https://github.com/billtrn/dsplot/blob/master/img/color_tree.png?raw=true" alt="color_tree" width="400">
</p>

- Edge values for Graphs: <br>
For edge values, `str` and `int` data types are supported at the moment.
```python
from dsplot.graph import Graph

graph = Graph(
    {0: [1, 4, 5], 1: [3, 4], 2: [1], 3: [2, 4], 4: [], 5: []},
    directed=True,
    edges={'01': 1, '04': 4, '05': 5, '13': 3, '14': 4, '21': 2, '32': 3, '34': 4},
)
graph.plot()
```
<p align="center">
  <img src="https://github.com/billtrn/dsplot/blob/master/img/edge_graph.png?raw=true" alt="edge_graph" width="300">
</p>

## 🎁 Bonus
### 1. Tree traversals:
```python
from dsplot.tree import BinaryTree

tree = BinaryTree(nodes=[5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1])

print(tree.preorder())
# [5, 4, 11, 7, 2, 8, 13, 4, 5, 1]

print(tree.inorder())
# [7, 11, 2, 4, 5, 13, 8, 5, 4, 1]

print(tree.postorder())
# [7, 2, 11, 4, 13, 5, 1, 4, 8, 5]
```
### 2. Graph traversals:
```python
from dsplot.graph import Graph

graph = Graph(
    {0: [1, 4, 5], 1: [3, 4], 2: [1], 3: [2, 4], 4: [], 5: []}, directed=True
)

print(graph.bfs())
# [0, 1, 4, 5, 3, 2]

print(graph.dfs())
# [0, 1, 3, 2, 4, 5]
```
## 🤝 Contributing
Contributions, issues and feature requests are welcome! <br>
### Development setup
- `DSPlot` uses `poetry` for dependency management. For guidance on how to install `poetry`, please refer to the [official documentation](https://python-poetry.org/docs/#installation).
- After cloning the repo, run `poetry install` to install the dependencies.
### Running tests
- `DSPlot` uses `pytest` for testing. To run the tests, run `poetry run pytest` in the root directory.

## 📄 License
[MIT](./LICENSE)
