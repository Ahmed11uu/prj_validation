from abc import ABC, abstractmethod

#abstract class defining basic graph structure
class RootedGraph(ABC):
    def __init__(self):
        self.graph = dict()
        self.roots = []

    @abstractmethod
    def getRoots(self):
        pass
    
    @abstractmethod
    def getNeighbors(self, n):
        pass
    