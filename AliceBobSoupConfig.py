from souplanguage import SoupConfiguration

class AliceBobConf(SoupConfiguration):
    """
    Class representing a configuration for the interaction between Alice and Bob.
    """

    def __init__(self):
        self.state_Alice = 0   # 0, 1, 2
        self.state_Bob = 0

    def __hash__(self):
        """
        Compute the hash value for the instance.

        Returns:
        - The hash value.
        """
        return hash(self.state_Alice + self.state_Bob)

    def __eq__(self, other):
        """
        Check if two instances are equal.

        Parameters:
        - other: The other instance to compare.

        Returns:
        - True if the instances are equal; False otherwise.
        """
        return self.state_Alice == other.state_Alice and self.state_Bob == other.state_Bob

    def __str__(self):
        """
        Get a string representation of the instance.

        Returns:
        - A string representation.
        """
        return "Alice: " + str(self.state_Alice) + " Bob: " + str(self.state_Bob)
