#!/usr/bin/env python
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
                 # FIXME: realmente preciso inicializa-los como None
                 # aqui?
                 Q = None,
                 gammaPRQL = None): # FIXME: melhorar esse comentatio
                                    # (de repente fazer uma
                                    # documentacao?).
                                    # 
                                    # gamma used for PRQLearning
                                    # algorithm

        # Internal objects used in the algorithm
        #
        # FIXME: talvez fosse mais interessante haver um metodo que
        # inicializa todos esses objetos internamente (mais "clean",
        # talvez? - o que o PEP fala sobre isso?)
        self.MDP = MDP
        self.Agent = Agent
        self.Q = Q
        self.V_star = None

        #Learning parameters
        self.alpha = alpha
        self.gamma = gamma
        self.gammaPRQL = gammaPRQL
        self.epsilon = epsilon
        self.epsilonIncrement = epsilonIncrement
        self.K = K
        self.H = H

    def execute(self):
        # FIXME: utilizar tudo a partir do "self": evitar
        # ambiguidades. (nao vai ficar muito poluido desse jeito?)
        myAgent = self.Agent
        myMDP = self.MDP
        A = self.MDP.A

        self.initializeQ()
        Q = self.Q

        alpha            = self.alpha
        gamma            = self.gamma
        gammaPRQL        = self.gammaPRQL
        epsilon          = self.epsilon
        epsilonIncrement = self.epsilonIncrement

        # FIXME: choose better names and eventualy add some explanation
        # about W2 and Ws
        W2 = 0
        Ws = []
        for k in range(self.K):
            W = 0
            myAgent.setInitialState()
            for h in range(self.H):
                # Observes the current state
                s = myAgent.state

                # If it is a goal state, the episode ends
                if s in myMDP.G: break

                randomNumber = random()
                # Chooses an action following a epsilon-greedy
                # strategy.
                # 
                # FIXME: clarify this if and the meaning behind it in
                # the context of our work in LTI
                if randomNumber > epsilon:
                    # greedy
                    a = myAgent.selectBestAction(s, source = 'Q-Table', Q = Q)
                else:
                    # random
                    a = myAgent.selectRandomAction()

                # Executes the action, observes the reward received
                # and the new state
                s2, r = myAgent.executeAction(a)

                # FIXME: manter um vetor V com os maximos. Aqui acho
                # que seria interessante ter uma classe so para o V,
                # que teria um metodo de obtencao de V*(a)
                maxValue = -1.0
                for a2 in A:
                    if Q[s2][a2] > maxValue:
                        maxValue = Q[s2][a2]

                # Update the table entry for Q(s, a)
                # FIXME: quebrar essa conta em duas partes, uma do
                # alpha, outra sem. Guardar esses dois valores em
                # variavies com nomes significativos ()
                Q[s][a] = (1.0 - float(alpha)) * float(Q[s][a]) + \
                          float(alpha) * (float(r) + float(gamma) * float(maxValue))

                # Sets the current state as the new one
                myAgent.state = s2

                # FIXME: Add some comment here!
                # FIXME: Does it make sense for gammaPRQL to be different
                # from gamma in any circumstance? If not, delete this
                # and use gamma here.
                if gammaPRQL != None:
                    # FIXME: put a better comment here
                    # accumulate gamma on W (this value is used only in PRQLearning)
                    W = float(W) + pow(gammaPRQL, h) * r

            epsilon = epsilon + epsilonIncrement

            W2 = ( (W2 * k) + W ) / (k + 1)
            Ws.append(W2)

        self.Q = Q
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
