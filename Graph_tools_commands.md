# Python commands for Graph tools

## Start anaconda enviroment

```
conda activate gt
```

## Graph tools commands

### Generate a edge list from a csv file

```
from utils import *

...

my_edge_list = retrieve_edge_list_from_file(<filename>)
```

### Generate a graph with graph tool

```
g = Graph(directed=True/False)
```

### Add egdes to graph

```
g.add_edge_list( edge_list:[(source, target)] )
```
where both `source` and `target` are vertex indexes

### Add nodes to graph

```
g.add_node_list(<NodeList>:List)
```

