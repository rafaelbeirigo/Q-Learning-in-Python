#-*- coding: utf-8 -*-
#!/usr/bin/env python2
import operator
import numpy as np
from random import random

class QLearning:
    def __init__(self,
                 MDP,
                 Agent,
                 alpha,
                 gamma,
                 epsilon,
                 epsilonIncrement,
                 K,
                 H,
                 Q=None):

        # Internal objects used in the algorithm
        #
        # FIXME: talvez fosse mais interessante haver um metodo que
        # inicializa todos esses objetos internamente (mais "clean",
        # talvez? - o que o PEP fala sobre isso?)
        self.MDP = MDP
        self.Agent = Agent
        self.Q = Q

        self.V_star = {}
        for s in self.MDP.S:
            self.V_star[s] = 0.0

        #Learning parameters
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.epsilonIncrement = epsilonIncrement
        self.K = K
        self.H = H

    def execute(self):
        self.initializeQ()

        # FIXME: choose better names and eventualy add some explanation
        # about W2 and Ws
        W2 = 0
        Ws = []
        for k in range(self.K):
            W = 0
            self.Agent.setInitialState()
            for h in range(self.H):
                # Observes the current state
                s = self.Agent.state

                # If it is a goal state, the episode ends
                if s in self.MDP.G: break

                randomNumber = random()
                # Chooses an action following a epsilon-greedy
                # strategy.
                #
                # FIXME: clarify this if and the meaning behind it in
                # the context of our work in LTI
                if randomNumber <= self.epsilon:
                    # random
                    a = self.Agent.selectRandomAction()
                else:
                    # greedy
                    a = self.Agent.selectBestAction(s, source='Q-Table',
                                                    Q=self.Q)

                # Executes the action, observes the reward received
                # and the new state
                s2, r = self.Agent.executeAction(a)

                # Update the table entry for Q(s, a)
                # (1 - alpha) * Q[s][a] + alpha  * (r + gamma * V_star[s2])
                self.Q[s][a] = (1.0 - float(self.alpha)) * float(self.Q[s][a]) + \
                               float(self.alpha) * (float(r) + float(self.gamma) * float(self.V_star[s2]))

                # If this is the case, updates V_star[s]
                if self.Q[s][a] > self.V_star[s]:
                    self.V_star[s] = self.Q[s][a]

                # Sets the current state as the new one
                self.Agent.state = s2

                # Calculates the cummulative discounted reward gained
                # so far
                W = float(W) + pow(self.gamma, h) * r

            self.epsilon += self.epsilonIncrement

            W2 = ( (W2 * k) + W ) / (k + 1)
            Ws.append(W2)

        return W2, Ws

    def obtainPolicy(self):
        S = self.MDP.S
        Policy = {}
        for s in S:
            a = self.Agent.selectBestAction(s, source = 'Q-Table', Q = self.Q)
            Policy[s] = a

        self.Policy = Policy

    def printQ(self, fileName = None):
        Q = self.Q

        if fileName != None:
            f = open(fileName, 'w')

        for s in self.MDP.S:
            if fileName != None:
                f.write('\n' + s + '\n')
            else:
                print '\n', s

            for a in Q[s].iterkeys():
                if fileName != None:
                    f.write(a + ' ' + str(Q[s][a]) + '\n')
                else:
                    print a, Q[s][a]

        if fileName != None:
            f.close()

    def printPolicy(self, fileName = None):
        if fileName != None:
            f = open(fileName, 'w')

        for s in self.MDP.S:
            if f != None:
                f.write(s + ' ' + self.Policy[s] + '\n')
            else:
                print s, self.Policy[s]

        if fileName != None:
            f.close()

    def initializeQ(self):
        if self.Q == None:
            # For each state-action pair (s, a), initialize the table
            # entry Q(s, a) to zero
            Q = {}
            S = self.MDP.S
            A = self.MDP.A
            for s in S:
                Q[s] = {}
                for a in A:
                    Q[s][a] = 0.0
            self.Q = Q
