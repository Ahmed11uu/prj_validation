
#module containing utilty functions

from collections import deque

#traversal BFS
def bfsSearch(graph, query):
    visited = set()
    queue = deque()

    for root in graph.getRoots():
        queue.append(root)

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)

            if query(node):
                return node,visited

            unvisited = [n for n in graph.getNeighbors(node) if n not in visited]
            queue.extend(unvisited)
    return None,visited

#function to print the visited nodes
def print_visited_nodes_hanoi(searchResult):
    print("BFS search visited nodes: \n\n")
    for e in searchResult[1]:
            print(e.towers)