# OneBitClock.py

from Semantics import SemanticRelation

class OneBitClock(SemanticRelation):
    """
    Class representing a one-bit clock.

    Inherits from the SemanticRelation class.
    """

    def __init__(self):
        """
        Initialize a OneBitClock instance.

        Calls the constructor of the base class.
        """
        super().__init__()

    def initial(self):
        """
        Get the initial state of the one-bit clock.

        Returns:
        - A list containing the initial state.
        """
        return [0]

    def actions(self, conf):
        """
        Get the possible actions for the given state of the one-bit clock.

        Parameters:
        - conf: The current state of the one-bit clock.

        Returns:
        - A list containing the possible actions.
        """
        actions = []

        if conf == 1:
            actions.append(lambda _: [0])  # Use _ as an unused argument
        elif conf == 0:
            actions.append(lambda _: [1])

        return actions

    def execute(self, action, conf):
        """
        Execute the given action on the current state of the one-bit clock.

        Parameters:
        - action: The action to be executed.
        - conf: The current state of the one-bit clock.

        Returns:
        - The result of executing the action on the current state.
        """
        return action(conf)
