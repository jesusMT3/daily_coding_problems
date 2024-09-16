"""
The transitive closure of a graph is a measure of which vertices
are reachable from other vertices. It can be represented as a matrix M, 
where M[i][j] == 1 if there is a path between vertices i and j, and otherwise 0.

For example, suppose we are given the following graph in adjacency list form:

graph = [
    [0, 1, 3],
    [1, 2],
    [2],
    [3]
]
The transitive closure of this graph would be:

[1, 1, 1, 1]
[0, 1, 1, 0]
[0, 0, 1, 0]
[0, 0, 0, 1]
Given a graph, find its transitive closure.
"""
import numpy as np

def transitive_closure(graph: np.array):
    """Finds the transitive closure of an input graph."""
    # build transitive closure matrix
    closure = np.zeros([len(graph), len(graph)])

    # compare each combination of nodes
    for i in range(0, len(graph)):
        for j in range(0, len(graph)):

            # if there is a path from i to j, write a 1
            if bfs(graph, i, j):
                closure[i][j] = 1

    # return transitive closure matrix
    return closure

def bfs(graph, node, target_node):
    """Implement Bread First Search algorithm"""
    visited = []
    queue = []
    # initialization: enqueue the source node and mark as visited
    queue.append(node)
    visited.append(node)
    # exploration
    while len(queue) > 0:
        # dequeue a node
        actual_node = queue.pop(0)
        # check if it found a solution
        if actual_node == target_node:
            return True

        # run through unvisited neighbors
        for neighbor in graph[actual_node]:
            if neighbor not in visited:
                # enqueue the neighbor and mark as visited
                queue.append(neighbor)
                visited.append(neighbor)

    # return false because queue is empty and no path was found
    return False


if __name__ == "__main__":
    example_graph = [[0, 1, 3],
                     [1, 2],
                     [2],
                     [3]]

    # test BFS
    assert bfs(example_graph, 0, 2) is True
    assert bfs(example_graph, 0, 0) is True
    assert bfs(example_graph, 1, 3) is False

    # test transitive_closure
    solution = transitive_closure(example_graph)
    print(solution)
