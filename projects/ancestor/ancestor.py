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
    # add edges, but switcheroo for dft algorithm
    for relationship in ancestors:
        graph.add_edge(relationship[1], relationship[0])

    # make a list of the dft path
    path = graph.dft(starting_node)

    # check distance 
    if len(path) > 2:
        dist1 = graph.dfs(starting_node, path[-1])
        dist2 = graph.dfs(starting_node, path[-2])

    # checks and returns
    if len(path) < 2:
        return -1
    elif len(path) > 2:
        if len(dist1) == len(dist2):
            if path[-2] < path[-1]:
                return path[-2]
        else:
            return path[-1]
    else:
        return path[-1]



if __name__ == '__main__':
    earliest_ancestor(test_ancestors, 8)
    