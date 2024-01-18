# Semantics.py

from abc import ABC, abstractmethod

class SemanticRelation(ABC):
    """
    Abstract base class for semantic relations.

    Defines abstract methods that must be implemented by subclasses.
    """

    @abstractmethod
    def __init__(self):
        """
        Abstract constructor method.
        """
        pass

    @abstractmethod
    def initial(self):
        """
        Abstract method to get the initial state.

        Returns:
        - The initial state.
        """
        pass

    @abstractmethod
    def actions(self, src):
        """
        Abstract method to get possible actions for a given state.

        Parameters:
        - src: The current state.

        Returns:
        - A list containing possible actions.
        """
        pass

    @abstractmethod
    def execute(self, actions, src):
        """
        Abstract method to execute an action on the current state.

        Parameters:
        - actions: The action to be executed.
        - src: The current state.

        Returns:
        - The result of executing the action on the current state.
        """
        pass
