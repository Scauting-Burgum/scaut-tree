# scaut-tree
A node-tree library for Python.

# Installation
`scaut-tree` currently consists of two modules;
* `common` (common.py)
* `output` (output.py)

The `common` module is the only neccesary module,  
you can use the other modules to extend the functionality of `scaut-tree`.

Any of the aforementioned modules can be installed by placing the corresponding files in your project's folder.

# Usage
## The `common` module
### Creating a tree
```python
from common import Node

root = Node([
    Node(), 
    Node([
        Node(), Node(), Node()
    ])
])
```

This resulting tree looks like this;
```
Node
|-Node
|-Node
||-Node
||-Node
||-Node
```
