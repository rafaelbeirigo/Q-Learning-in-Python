#!/usr/bin/env python
import random

class Agent:
    def __init__(self, MDP = None, state = None):
        self.MDP = MDP
        self.state = state
        
    def executeAction(self, a):
        s2, r = self.MDP.executeAction(a, self.state)

        return s2, r

    def selectRandomAction(self):
        # look at all the possible transitions T[s][a][s']
        # where s == self.state and then gather the possible
        # actions for the current state
        T = self.MDP.T
        s = self.state
        A = []
        for a in T[s].iterkeys():
            for s2 in T[s][a].iterkeys():
                if T[s][a][s2] > 0:
                    A.append(a)

        # obtain a random action
        a = random.choice(A)

        return a

    def selectBestAction(self, s = None, Q = None):
        # look at all the possible transitions T[s][a][s']
        # where s == self.state and then gather the possible
        # actions for the current state
        T = self.MDP.T
        if s == None:
            s = self.state
        A = []
        for a in T[s].iterkeys():
            for s2 in T[s][a].iterkeys():
                if T[s][a][s2] > 0.0:
                    A.append(a)

        # obtain the best possible value using the possible
        # actions for the state
        maxValue = -1.0
        for a in A:
            if Q[s][a] > maxValue:
                maxValue = Q[s][a]

        # obtain all the actions whose value equals the maximum
        B = []
        for a in A:
            if Q[s][a] == maxValue:
                B.append(a)

        # obtain a random action
        if len(B) > 0:
            a = random.choice(B)
        else:
            a = '---'

        return a

    def setInitialState(self):
      self.state = random.choice(self.MDP.S)
