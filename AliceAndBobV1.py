import random
from Semantic import Semantic


class AliceAndBobV1(Semantic):

    def __init__(self):
        self.fA=0   #flag
        self.fB=0

    def initial(self):
        return [("initialAlice", "initialBob")]

    def actions(self, config):
        a=[]
        print("start ")
        print(config)
        # if random.random() < 0.5: #alice moves
        #     # print("moma ")
        #     # print(type(config))
        #     al,b=config
        #     print("alice moves")
        #     if al == "initialAlice":
        #         a.append(lambda x: [("attendAlice",b)])
        #     elif al == "attendAlice":
        #         a.append(lambda x: [("EnSectionCritiqueAlice",b)])
        #     elif al == "EnSectionCritiqueAlice":
        #         a.append(lambda x: [("initialAlice",b)])
        # else:#bob moves
        #     al,b=config
        #     print("bob moves")
        #     if b == "initialBob":
        #         a.append(lambda x: [(al,"attendBob")])
        #     elif b == "attendBob":
        #         a.append(lambda x: [(al,"EnSectionCritiqueBob")])
        #     elif b == "EnSectionCritiqueBob":
        #         a.append(lambda x: [(al,"initialBob")])
        # print("end ")


        #test 2

        
        al,b=config
        # print("alice moves")
        if al == "initialAlice":
            a.append(lambda x: [("attendAlice",b)])
            self.fA=1
        elif al == "attendAlice" and self.fB==0:
            a.append(lambda x: [("EnSectionCritiqueAlice",b)])
        elif al == "EnSectionCritiqueAlice":
            a.append(lambda x: [("initialAlice",b)])
            self.fA=0
    
        # print("bob moves")
        if b == "initialBob":
            a.append(lambda x: [(al,"attendBob")])
            self.fB=1
        elif b == "attendBob" and self.fA==0:
            a.append(lambda x: [(al,"EnSectionCritiqueBob")])
        elif b == "EnSectionCritiqueBob":
            a.append(lambda x: [(al,"initialBob")])
            self.fB=0
        print("end ")

        return a

    def execute(self, action, config):
        return action(config)
    
    
