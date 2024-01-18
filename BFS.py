# bfs.py

from collections import deque

def bfs_search(graph, query):
    """
    Perform Breadth-First Search on a graph to find a node satisfying a given query.

    Parameters:
    - graph: The graph on which BFS is performed.
    - query: A function that takes a node and returns True if the node satisfies the query.

    Returns:
    - A tuple containing the found node and the set of visited nodes.
    """
    visited = set()
    queue = deque()
    i = True  # Flag to handle the initial case when starting from roots

    while queue or i:
        if i:
            neighbours = graph.getRoots()
            i = False
        else:
            neighbours = graph.getNeighbors(queue.popleft())

        for neighbour in neighbours:
            if neighbour not in visited:
                if query(neighbour):
                    return neighbour, visited
                visited.add(neighbour)
                queue.append(neighbour)

    # If no matching node is found
    return None, visited
