# SoupSemantics.py

from abc import ABC, abstractmethod
from typing import List

from Semantics import SemanticRelation

class SoupConfiguration(ABC):
    """
    Abstract base class for soup configurations.
    """

    @abstractmethod
    def __hash__(self):
        pass

    @abstractmethod
    def __eq__(self, other: object):
        pass

    @abstractmethod
    def __repr__(self):
        pass

class Piece:
    """
    Class representing a piece in a soup configuration.
    """

    def __init__(self, name: str, guard, action):
        self.name = name
        self.guard = guard
        self.action = action

    def enabled(self, config):
        """
        Check if the piece is enabled in a given configuration.

        Parameters:
        - config: The soup configuration.

        Returns:
        - True if the piece is enabled; False otherwise.
        """
        return self.guard(config)

    def execute(self, config):
        """
        Execute the action of the piece on a given configuration.

        Parameters:
        - config: The soup configuration.

        Returns:
        - A list containing the result of executing the action.
        """
        return [self.action(config)]

class SoupSpec:
    """
    Class representing the specification of a soup.
    """

    def __init__(self, pieces, initials):
        self.initials = initials
        self.pieces_list = pieces

    def initial(self):
        """
        Get the initial configurations of the soup.

        Returns:
        - A list of SoupConfiguration instances.
        """
        return self.initials

    def pieces(self) -> List[Piece]:
        """
        Get the list of pieces in the soup.

        Returns:
        - A list of Piece instances.
        """
        return self.pieces_list

    def enabledPieces(self, c):
        """
        Get the enabled pieces in a given configuration.

        Parameters:
        - c: The soup configuration.

        Returns:
        - A list of enabled Piece instances.
        """
        filtered_pieces = list(filter(lambda p: p.enabled(c), self.pieces_list))
        return filtered_pieces

class SoupSemantics(SemanticRelation):
    """
    Class representing the semantics of the soup.
    """

    def __init__(self, spec):
        self.spec = spec

    def initial(self):
        """
        Get the initial configurations of the soup.

        Returns:
        - A list of SoupConfiguration instances.
        """
        return self.spec.initial()

    def actions(self, config):
        """
        Get the enabled pieces in a given configuration.

        Parameters:
        - config: The soup configuration.

        Returns:
        - A list of enabled Piece instances.
        """
        return self.spec.enabledPieces(config)

    def execute(self, action, config):
        """
        Execute the action of a piece on a given configuration.

        Parameters:
        - action: The action (Piece) to be executed.
        - config: The soup configuration.

        Returns:
        - A list containing the result of executing the action.
        """
        return action.execute(config)
