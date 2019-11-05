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
1. V is verticies
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


