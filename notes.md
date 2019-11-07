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

Graphs are a set of vertices and edges that connect those vertices. We can use graphs to represent a variety of different networks or related pieces of data.

## Breadth First Search

![Breadth First Search](https://i.imgur.com/7Mn3r52.jpg)

1. Is an algorithm used to search a graph--and find a solution to whatever we are trying to solve.

2. Explores all possible paths to find one with the smallest weight, traversing across before traversing down.

3. In breadth-first search we explore all the nodes on the same level of the graph before moving down to deeper levels that are further away from the root.

4. The algorithm never attempts to explore a vert that it either has explored or is exploring.

### Uses

1. Route finding or path finding problems
   1. Makes sense to explore the closest routes first
2. Social network
   1. Friend suggestions on Facebook
   2. connect suggestions on linkedin

### Algorithm

1. Begin at the starting vertex(s)
   1. If tree, it starts at root of tree
   2. If undirected graph, define a start
2. Explore vertex 
   1. You're at a specific vertex and you're going to explore it using a loop that you're repeating over and over
   2. while there is at least 1 other vertex adjacent to this that we have not marked to explore
      1. We're going to schedule that vertex to be explored later
         1. you can use a `[ queue ]` to implement that scheduling
         2. continue to schedule adjacent vertices to current vertex
3. Mark vertex as explored
   1. Once you're finished scheduling all the vertices
   2. You can now mark vertices as explored, and remove them from queue





