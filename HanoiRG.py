# HanoiRG.py

from collections import deque
from RootedGraph import RootedGraph
from HanoiConfig import HanoiConfig, isFinal
from ParentTracer import ParentTraceur
from BFS import bfs_search

# Implementation of the graph with nodes representing Hanoi configurations
class HanoiRG(RootedGraph):
    """
    Class representing a rooted graph for the Towers of Hanoi problem.

    Inherits from the RootedGraph class.

    Attributes:
    - graph: A dictionary representing the graph structure.
    - roots: A list containing the root nodes of the graph (HanoiConfig instances).
    """

    def __init__(self):
        """
        Initialize a HanoiRG instance with an empty graph and a single root node (HanoiConfig instance).
        """
        self.graph = dict()
        self.roots = [HanoiConfig(3)]  # Roots of the graph

    def add_edge(self, u, v):
        """
        Add a directed edge between nodes u and v in the graph.

        Parameters:
        - u: The source node.
        - v: The destination node.
        """
        self.graph.setdefault(u, []).append(v)  # Add an edge between nodes u and v

    def getRoots(self):
        """
        Get the root nodes of the graph.

        Returns:
        - A list containing the root nodes (HanoiConfig instances).
        """
        return self.roots

    def getNeighbors(self, n):
        """
        Get the neighbors of a given node in the graph.

        Parameters:
        - n: The node for which neighbors are to be retrieved.

        Returns:
        - A list containing the neighbors (HanoiConfig instances) of the specified node.
        """
        neighbors = []

        # Move a disk to another tower
        for source in range(3):
            for destination in range(3):
                if source != destination and n.is_valid_move(source, destination):
                    new_config = n.move_disk_and_get_next_state(source, destination)
                    neighbors.append(new_config)

        return neighbors
