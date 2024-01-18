# DictRootedGraph.py

from BFS import bfs_search
from RootedGraph import RootedGraph

class DictRootedGraph(RootedGraph):
    """
    A class representing a rooted graph using a dictionary-based approach.

    Inherits from the RootedGraph class.

    Attributes:
    - graph: A dictionary representing the graph structure.
    - roots: A list containing the root nodes of the graph.
    """

    def __init__(self):
        """
        Initialize a DictRootedGraph with an empty graph and no roots.
        """
        self.graph = dict()
        self.roots = []

    def getRoots(self):
        """
        Get the root nodes of the graph.

        Returns:
        - A list containing the root nodes.
        """
        return self.roots

    def getNeighbors(self, node):
        """
        Get the neighbors of a given node in the graph.

        Parameters:
        - node: The node for which neighbors are to be retrieved.

        Returns:
        - A list containing the neighbors of the specified node.
        """
        return self.graph.get(node, [])

    def add_new_one(self, u, v):
        """
        Add a new directed edge from node u to node v in the graph.

        Parameters:
        - u: The source node.
        - v: The destination node.
        """
        self.graph.setdefault(u, []).append(v)
        # Adds an edge between u and v in the graph.
        # Checks if u does not exist, initializes it with an empty list before adding v.

    def __eq__(self, other):
        """
        Check if two DictRootedGraph instances are equal.

        Parameters:
        - other: The other instance to compare.

        Returns:
        - True if the instances are of the same type and have equal 'graph' and 'roots' attributes; False otherwise.
        """
        is_same_type = type(other) is DictRootedGraph
        same_graph = self.graph == other.graph
        same_roots = self.roots == other.roots
        return is_same_type and same_graph and same_roots

    def __hash__(self):
        """
        Compute the hash value for the instance.

        Returns:
        - A constant hash value (1) for simplicity.
        """
        return 1
