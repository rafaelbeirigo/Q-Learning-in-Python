#!/usr/bin/env python2
# This is going to be one of the learning algorithms that I will use
# Well, I have then the choice given by the modularity
import operator
import numpy as np
# teste.a
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
                 Q = None,
                 gammaPRQL = None): #gamma used for PRQLearning algorithm
        
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

        W2 = 0
        Ws = []
        for k in range(self.K):
            W = 0
            myAgent.setInitialState()
            #myAgent.state = '1'
            for h in range(self.H):
                # TODO: remover os '---'
                # ---Observe the current state s
                s = myAgent.state

                # if a goal state is reached the episode ends
                if s in myMDP.G: break

                # ---Following epsilon-greedy strategy,
                # ---Select an action a and execute it
                # ---Receive immediate reward r
                # ---Observe the new state s2
                randomNumber = random()
                if randomNumber <= epsilon:
                    # random
                    a = myAgent.selectRandomAction()
                else:
                    # greedy
                    a = myAgent.selectBestAction(s, source = 'Q-Table', Q = Q)

                s2, r = myAgent.executeAction(a)

                # TODO: manter um vetor V com os maximos
                maxValue = -1.0
                for a2 in A:
                    if Q[s2][a2] > maxValue:
                        maxValue = Q[s2][a2]

                # ---Update the table entry for Q(s, a)
                Q[s][a] = (1.0 - float(alpha)) * float(Q[s][a]) + \
                          float(alpha) * (float(r) + float(gamma) * float(maxValue))
				
                # ---s=s'
                myAgent.state = s2

                if gammaPRQL != None:
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
            # For each state-action pair (s, a), initialize the table entry Q(s, a) to zero
            Q = {}
            S = self.MDP.S
            A = self.MDP.A
            for s in S:
                Q[s] = {}
                for a in A:
                    Q[s][a] = 0.0
            self.Q = Q
