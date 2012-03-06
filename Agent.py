#!/usr/bin/env python
import random

class Agent:
    def __init__(self, MDP = None, state = None):
        self.MDP = MDP
        self.state = state
        
    def executeAction(self, a):
        r, s = self.MDP.executeAction(a, self.state)

        return r, s

    def selectAction(self):
        a = None

        #look at all the possible transitions T[s][a][s']
        #where s == self.state
        #obtem todas as acoes possiveis para o estado atual
        A = self.MDP.T[self.state]
        A1 = []
        for a1 in A.iterkeys():
            for s1 in A[a1].iterkeys():
                if A[a1][s1] > 0:
                    A1.append(a1)

        print "selectAction"
        print "s: " + self.state
        print "acoes possiveis:"
        print A1
        #sorteia uma acao dentre as possiveis
        a = random.choice(A1)
        print "acao escolhida: " + a
        return a

    def setInitialState(self):
      self.state = random.choice(self.MDP.S)
