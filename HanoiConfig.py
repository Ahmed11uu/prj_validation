# HanoiConfig.py

import copy

class HanoiConfig:
    """
    Class representing the configuration of the Towers of Hanoi problem.

    Attributes:
    - towers: List of three towers containing the disk configurations.
    """

    def __init__(self, n):
        """
        Initialize a HanoiConfig instance with 'n' disks.

        Parameters:
        - n: The number of disks in the Towers of Hanoi problem.
        """
        tower1 = list(range(n, 0, -1))
        tower2 = list()
        tower3 = list()
        self.towers = [tower1, tower2, tower3]

    def is_valid_move(self, source_index, destination_index):
        """
        Check if moving a disk from the source tower to the destination tower is a valid move.

        Parameters:
        - source_index: Index of the source tower.
        - destination_index: Index of the destination tower.

        Returns:
        - True if the move is valid; False otherwise.
        """
        source_tower = self.towers[source_index]
        destination_tower = self.towers[destination_index]

        if not source_tower:
            return False
        else:
            if not destination_tower or source_tower[-1] < destination_tower[-1]:
                return True
            else:
                return False

    def move_disk_and_get_next_state(self, source_index, destination_index):
        """
        Move a disk from the source tower to the destination tower and get the next configuration.

        Parameters:
        - source_index: Index of the source tower.
        - destination_index: Index of the destination tower.

        Returns:
        - A new HanoiConfig instance representing the next configuration after the move.
        """
        next_state = copy.deepcopy(self)
        next_state.towers[destination_index].append(next_state.towers[source_index].pop())
        return next_state

    def __hash__(self):
        """
        Compute the hash value for the instance.

        Returns:
        - A constant hash value (1) for simplicity.
        """
        return 1

    def __eq__(self, other):
        """
        Check if two HanoiConfig instances are equal.

        Parameters:
        - other: The other instance to compare.

        Returns:
        - True if the instances have equal 'towers' attributes; False otherwise.
        """
        return self.towers == other.towers


def is_empty_towers(towers):
    """
    Check if all towers in the list are empty.

    Parameters:
    - towers: List of towers.

    Returns:
    - True if all towers are empty; False otherwise.
    """
    return all(len(tower) == 0 for tower in towers)


def is_sorted_descending(tower):
    """
    Check if a tower is sorted in descending order.

    Parameters:
    - tower: The tower to check.

    Returns:
    - True if the tower is sorted in descending order; False otherwise.
    """
    return all(tower[i] > tower[i + 1] for i in range(len(tower) - 1))


def isFinal(node):
    """
    Check if a node represents the final state of the Towers of Hanoi problem.

    Parameters:
    - node: The HanoiConfig instance to check.

    Returns:
    - True if the node represents the final state; False otherwise.
    """
    return is_empty_towers(node.towers[:2]) and is_sorted_descending(node.towers[2])
