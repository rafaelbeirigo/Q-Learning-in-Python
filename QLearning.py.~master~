#!/usr/bin/env python
# This is going to be one of the learning algorithms that I will use
# Well, I have then the choice given by the modularity
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
                 numberOfSteps,
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
        self.numberOfSteps = numberOfSteps
        
    def execute(self):
        myAgent = self.Agent
        myMDP = self.MDP
        
        # Q-Table initialization
        if self.Q == None:
            # For each state-action pair (s, a), initialize the table entry Q(s, a) to zero
            Q = {}
            S = self.MDP.S
            A = self.MDP.A
            for s in S:
                Q[s] = {}
                for a in A:
                    Q[s][a] = 0.00001717
            self.Q = Q
        else:
            # If one Q was received, use it
            Q = self.Q

        alpha            = self.alpha
        gamma            = self.gamma
        gammaPRQL        = self.gammaPRQL
        epsilon          = self.epsilon
        epsilonIncrement = self.epsilonIncrement
        
        W = 0
        for episode in range(self.numberOfEpisodes):
            for h in range(self.numberOfSteps):
                # ---Observe the current state s
                s = myAgent.state
                while s in myMDP.G:
                    myAgent.setInitialState()
                    s = myAgent.state

                # ---Following epsilon-greedy strategy,
                # ---Select an action a and execute it
                # ---Receive immediate reward r
                # ---Observe the new state s2
                randomNumber = random()
                if randomNumber <= epsilon:
                    # greedy
                    a = myAgent.selectBestAction(s, Q)
                else:
                    # random
                    a = myAgent.selectRandomAction()

                s2, r = myAgent.executeAction(a)

                maxValue = -1.0
                for a2 in A:
                    if Q[s2][a2] > maxValue:
                        maxValue = Q[s2][a2]

                # ---Update the table entry for Q(s, a)
                Q[s][a] = (1.0 - float(alpha)) * float(Q[s][a]) + \
                          float(alpha) * (float(r) + float(gamma) * float(maxValue))

                # ---s=s'
                myAgent.state = s2
                epsilon = epsilon + epsilonIncrement

                if gammaPRQL != None:
                    # accumulate gamma on W (this value is used only in PRQLearning)
                    W = float(W) + pow(gammaPRQL, h) * r
                
        self.Q = Q
        return W

    def obtainPolicy(self):
        S = self.MDP.S
        Policy = {}
        for s in S:
            a = self.Agent.selectBestAction(s, self.Q)
            Policy[s] = a

        self.Policy = Policy

    def printQ(self, fileName = None):
        Q = self.Q

        if fileName != None:
            f = open(fileName, 'w')

        for s in self.MDP.S:
            print '\n', s
            if fileName != None: f.write('\n' + s + '\n')

            for a in Q[s].iterkeys():
                print a, Q[s][a]
                if fileName != None: f.write(a + ' ' + str(Q[s][a]) + '\n')

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
