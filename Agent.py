#!/usr/bin/env python
import random

class Agent:
    def __init__(self, MDP):
        self.MDP = MDP
        self.state = None

    def obtainPossibleActions(self):
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

        return A
        
    def executeAction(self, a):
        s2, r = self.MDP.executeAction(a, self.state)
        return s2, r

    def selectRandomAction(self):
        A = self.obtainPossibleActions()
        a = random.choice(A)

        return a

    def selectBestActionFromQTable(self, s, Q):
        A = self.obtainPossibleActions()
        
        # discover what is the best possible value considering
        # all possible actions for the state
        maxValue = -1.0
        for a in A:
            if Q[s][a] > maxValue:
                maxValue = Q[s][a]

        # obtain all the actions whose value equals the maximum
        B = []
        for a in A:
            if Q[s][a] == maxValue:
                B.append(a)

        # obtain a random action from all the possible ones
        if len(B) > 0:
            a = random.choice(B)
        else:
            a = '---'

        return a

    def selectBestActionFromProbPolicy(self, s, Pi):
        P = []
        acum = 0.0

        for a in Pi[s].iterkeys():
            if Pi[s][a] > 0.0:
                p = []
                p.append(a)
                acum = acum + Pi[s][a]
                p.append(acum)
                P.append(p)

        #sorteia um numero no intervalo [0, 1]
        x = random.random()

        for p in P:
            if x <= p[1]:
                a = p[0]
                break

        return a

    def selectBestAction(self, s, source = None, Q = None, Pi = None):
        if source == 'Q-Table':
            a = self.selectBestActionFromQTable(s, Q)
        elif source == 'Probabilistic Policy':
            a = self.selectBestActionFromProbPolicy(s, Pi)
        else:
            'ERROR: wrong source (' + source
            sys.exit(1)

        return a

    def setInitialState(self):
        if self.MDP.P == None:
            self.state = random.choice(self.MDP.S)
        else:
            self.state = self.setInitialStateByProb()

    def setInitialStateByProb(self):
        P = self.MDP.P
        P2 = []
        acum = 0.0

        for s in self.MDP.S:
            if P[s] > 0.0:
                p = []
                p.append(s)
                acum = acum + P[s]
                p.append(acum)
                P2.append(p)

        x = random.random()

        for p in P2:
            if x <= p[1]:
                s = p[0]
                break

        return s
