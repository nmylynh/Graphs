# Graphs

![graph](https://i.imgur.com/X3pYQxG.png "graph from lambda")

Are collections of data represented by nodes and connections between nodes.

## Components 

1. **nodes or vertices** - represent objects in a data set (citiies, animals, web pages)
   1. If you have location as a graph, the cities might be your nodes
   2. Animal hierarchy with different animals groups
   3. nodes that represent different pages on a website
2. **edges** - connections between vertices; can be bidirectional
   1. edges are connections between all those aforementioned different types of data
   2. edges might be the roads
   3. For the animal hierarchies example, you can have the general animal groups at the top and edges showing all the the different animals falling under that group
      1. e.g. node that represents mammals and then edges connecting mammals to different subclasses of mammals
   1. For webpages, from page A, what pages do I have the ability to get to
3. **weight** -cost to travel across an edge
   1. not all edges are created equal
   2. might cost more time or resources to get from one node to another
   3. we can represent that using weight

**Code for above image:**
1. V is verticies/nodes
2. E is edges
   1. in the front edge, `(v0, v1, 5)` represents the two verticies it connects to and the last number is the optional weight

```python

V = { V0, V1, V2, V2, V4, V5 }

E = { 
        (v0, v1, 5), (v1, v2, 4), 
        (v2, v3, 9), (v3, v4, 7),
        (v4, v0, 1), (v0, v5, 2),
        (v5, v4, 8), (v3, v5, 3),
        (v5, v2, 1)
    }
```

### Examples

#### BART

![sf bart map](https://www.bart.gov/sites/all/themes/bart_desktop/img/system-map.gif "sf bart map")

- In the above picture, the different possibile stops you can get off at are nodes
- The different trains to get to one stop to another are edges
- Each edges has a weight like
  - how much time it takes to get to one stop to another

#### Github

Networks of activity is made using graphs (push, pull, commits)

![github](https://eazybi.com/static/img/blog_page/posts/2016_01_21/git_log_analysis_and_reporting.png)

#### Any networks
- Social networks
- Cell phone networks
- etc.

#### Websites

![website](https://i.imgur.com/THnIATB.png)

1. **Directed graph**
   1. can only move in one direction along edges
2. **undirected graph/bidirectional graphs** 
   1. allows movement in both directions along edges 

#### Cyclic Graphs && Acyclic

![cyclic graph](https://study.com/cimages/multimages/16/cyclic_graphs.png)

>A cyclic graph is a directed graph which contains a path from at least one node back to itself. In simple terms cyclic graphs contain a cycle.

- Edges allow you to revisit at least one vert.

![acyclic](https://study.com/cimages/multimages/16/a6abfeb0-f4ea-48b3-ab1e-0891c880d74a_acyclic_graphs.png)

>An acyclic graph is a directed graph which contains absolutely no cycle, that is no node can be traversed back to itself.

- vertices can only be visited once

### In conclusion

Graphs are a set of vertices and edges that connect those vertices. We can use graphs to represent a variety of different netwroks or related pieces of data.