# AliceAndBob.py

# Import necessary modules
from BFS import bfs_search
from ParentTracer import ParentTraceur
from Semantics import SemanticRelation
from Semantics2RG import Semantics2RG

# Define the AliceetBobV1 class, inheriting from SemanticRelation
class AliceetBobV1(SemanticRelation):
    def __init__(self):
        super().__init__()
        self.flagAlice = 0
        self.flagBob = 0

    def initial(self):
        # Define the initial configuration for Alice and Bob
        return [("Home_Alice", "Home_Bob")]

    def actions(self, conf):
        actions = []
        confAlice, confBob = conf

        # Alice's actions
        if confAlice == "Home_Alice":
            actions.append(lambda state: [("Wait_Alice", state[1])])
        elif confAlice == "Wait_Alice" and confBob != "SC_Bob":
            actions.append(lambda state: [("SC_Alice", state[1])])
        elif confAlice == "SC_Alice":
            actions.append(lambda state: [("Home_Alice", state[1])])

        # Bob's actions
        if confBob == "Home_Bob":
            actions.append(lambda state: [(state[0], "Wait_Bob")])
        elif confBob == "Wait_Bob" and confAlice != "SC_Alice":
            actions.append(lambda state: [(state[0], "SC_Bob")])
        elif confBob == "Wait_Bob":
            actions.append(lambda state: [(state[0], "Home_Bob")])

        print(f"Conf: {conf}")
        return actions

    def execute(self, action, conf):
        # Execute the given action on the current configuration
        return action(conf)

# Entry point for the script
if __name__ == '__main__':
    # Instantiate the AliceetBobV1 coordinator
    coordinator = AliceetBobV1()

    # Create a rooted graph using Semantics2RG
    rg = Semantics2RG(coordinator)

    # Create a ParentTraceur for tracing parents in the graph
    traceur = ParentTraceur(rg)

    # Run BFS search to find a specific state
    w, k = bfs_search(traceur, lambda x: x[0] == "SC_Alice" and x[1] == "SC_Bob")

    # Get the trace of the found state
    trace = traceur.get_trace(w)
    print(trace)
