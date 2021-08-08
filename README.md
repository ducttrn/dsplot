# Data Structure Plot (DSPlot)
[![Build Status](https://travis-ci.com/billtrn/dsplot.svg?branch=master)](https://travis-ci.com/billtrn/dsplot)
[![Coverage Status](https://coveralls.io/repos/github/billtrn/dsplot/badge.svg?branch=master)](https://coveralls.io/github/billtrn/dsplot?branch=master)
[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/billtrn/dsplot/blob/master/LICENSE)

DSPlot is a tool to simply visualize tree and graph data structures by serving as a Pythonic interface to the [Graphviz](https://graphviz.org/) layout.
DSPlot allows you to easily draw trees and graphs (both directed and undirected) by passing data in primitive form and directly output an image.

## ⬇ Installation

#### 0. Prerequisites
- Python 3.7 or later
- `pip`
- `virtualenv`

#### 1. Install Graphviz
- MacOS:
```
brew install graphviz
```
- Linux:
```
apt-get install graphviz
```
- Other OS(s): https://graphviz.org/download/

#### 2. Install package
```
$ pip install dsplot
```

## 🤟 Usage
- Binary Tree:
```python
from dsplot.tree import BinaryTree

tree = BinaryTree(nodes=[5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1])
tree.plot()
```
![tree](https://github.com/billtrn/dsplot/blob/master/img/tree.png?raw=true)

- Graph:
```python
from dsplot.graph import Graph

graph = Graph(
    {0: [1, 4, 5], 1: [3, 4], 2: [1], 3: [2, 4], 4: [], 5: []}, directed=True
)
graph.plot()
```
![directed](https://github.com/billtrn/dsplot/blob/master/img/directed.png?raw=true)
```python
from dsplot.graph import Graph

graph = Graph(
    {1: [2, 4], 2: [1, 3], 3: [2, 4, 5], 4: [1, 3], 5: [3, 6, 7], 6: [5], 7: [5]}, directed=False
)
graph.plot()
```
![undirected](https://github.com/billtrn/dsplot/blob/master/img/undirected.png?raw=true)

## 🎁 Additional features
### 1. Tree traversals:
- Preorder
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
## 📄 License
[MIT](./LICENSE)
