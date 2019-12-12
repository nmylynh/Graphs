from util import Stack, Queue, Graph
"""

Write a function that, given the dataset and the ID of an individual in the dataset, returns their earliest known ancestor – the one at the farthest distance from the input individual. If there is more than one ancestor tied for "earliest", return the one with the lowest numeric ID. If the input individual has no parents, the function should return -1.
"""
test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]


def earliest_ancestor(ancestors, starting_node):
    graph = Graph()
    # populate graph with vertices
    for relationship in ancestors:
        graph.add_vertex(relationship[0])
        graph.add_vertex(relationship[1])
    # populate graph, for every rel tuple, add an edge connecting each appropriate vert[index]
    for relationship in ancestors:
        graph.add_edge(relationship[0], relationship[1])
        
    print(graph.vertices)


if __name__ == '__main__':
    earliest_ancestor(test_ancestors, 1)
    