from SoupLangage import SoupConfiguration


class AliceBobConf(SoupConfiguration):
    def __init__(self):
        self.state_Alice = 0   #0,1,2
        self.state_Bob = 0

    def __hash__(self):
        return hash(self.state_Alice + self.state_Bob)

    def __eq__(self, other):
        return self.state_Alice == other.state_Alice and self.state_Bob == other.state_Bob

    def __str__(self):
        return "Alice: "+str(self.state_Alice) +" Bob: "+ str(self.state_Bob)