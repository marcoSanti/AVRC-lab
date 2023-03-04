# Python commands for Graph tools

## Start anaconda enviroment

```
conda activate gt
```

## Graph tools commands

### Generate a edge list from a text file

```python
from utils import *

...

my_edge_list = retrieve_edge_list_from_file(filename)
```

### Import graph tool

```python
from gt.all import *
```

### Import a edge list from networks.skewed.de

```python
g = gt.collection.ns["terrorists_911"]
```


### Generate a graph with graph tool

```python
g = Graph(directed=True/False)
```

### Add egdes to graph

```python
g.add_edge_list( edge_list:[(source, target, weight=null,  )] )
```
where both `source` and `target` are vertex indexes

### Add nodes to graph

```python
g.add_node_list( node_list: [node_1, ... , node_n] )
```

### Get neighbor set

```python
g.get_all_neighbors( vertex )
```

### node Degree

```python
g.get_in_degree( vertex )
g.get_out_degree( vertex )
g.get_total_degree( vertexList )
```

### Get average degree

```python
gt.stats.get_vertex_average( graph, degree="in/out/total")
```

### Get node strength

```python
#in strength
sum( weigth for node_a, node_b, weigth in g.get_in_edges ( node ))

#out strength
sum( weigth for node_a, node_b, weigth in g.get_out_edges ( node ))
```

### Get shortest path

```python
gt.topology.shortest_path ( graph , source_node , target_node )
```

### Draw a graph

```python
gt.draw.graph_draw( graph )
```



