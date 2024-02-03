import random
from Semantic import Semantic


class AliceAndBob0(Semantic):

    def __init__(self):
        self.sA=0   #sA représente l'état actuel de Alice: 0:initial 1:attente 2:critique
        self.sB=0

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
        elif al == "attendAlice":
            a.append(lambda x: [("EnSectionCritiqueAlice",b)])
        elif al == "EnSectionCritiqueAlice":
            a.append(lambda x: [("initialAlice",b)])
    
        # print("bob moves")
        if b == "initialBob":
            a.append(lambda x: [(al,"attendBob")])
        elif b == "attendBob":
            a.append(lambda x: [(al,"EnSectionCritiqueBob")])
        elif b == "EnSectionCritiqueBob":
            a.append(lambda x: [(al,"initialBob")])
        print("end ")

        return a

    def execute(self, action, config):
        return action(config)
    
    
