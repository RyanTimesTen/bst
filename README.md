# bst
[![Build Status](https://travis-ci.org/rgilbert1/bst.svg?branch=master)](https://travis-ci.org/rgilbert1/bst)

In school, I struggled with how binary search trees (and related data structures & algorithms) work, but now with a little more programming experience under my belt I decided to work through implementing one. It currently has insert, search, and traversal functionality.

## Install

```
pip install bst
```

## Usage

```python
from bst import BST

bst = BST()
bst.insert(5)
node = bst.search(5)  # <bst.Node object at 0x1060964e0>
node.value  # 5
```

## Development

The only dependency is `nose`, it's used to automatically run all of the unit tests in `tests/`. Install dependencies with `pip install -r requirements.txt`, and run the tests with `nosetests -v`.
