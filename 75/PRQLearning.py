#!/usr/bin/env python

import QLearning
import operator
import csv
from math import exp
from random import random
from numpy import cumsum
from os import listdir

class PRQLearning:
    def __init__(self, \
                 MDP, \
                 Agent, \
                 alpha, \
                 gamma, \
                 epsilon, \
                 epsilonIncrement, \
                 K, \
                 H, \
                 gammaPRQL,
                 tau, \
                 deltaTau, \
                 psi, \
                 v, \
                 filePath):

        self.MDP = MDP
        self.Agent = Agent
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.epsilonIncrement = epsilonIncrement
        self.K = K
        self.H = H
        self.gammaPRQL = gammaPRQL
        self.tau = tau
        self.deltaTau = deltaTau
        self.psi = psi
        self.v = v
        self.filePath = filePath
        self.L = self.loadPolicies()
        self.myQLearning = None

    def execute(self):
        # Initialize
        # For each state-action pair (s, a), initialize the table
        # entry Q_omega(s, a) to zero
        # The W_omega from the article is W[omega], with omega == 0,
        # and the same applies to U_omega
        L = self.loadPolicies()

        Q_omega, W, U = self.initializeQ_omegaWU()

        myQLearning = self.initializeQLearning(Q = Q_omega)
        self.myQLearning = myQLearning

        logStuff = []
        logStuffTitle = []

        logStuffTitle.append('iteration')
        logStuffTitle.append('state')
        logStuffTitle.append('psi')
        logStuffTitle.append('randomNumber1')
        logStuffTitle.append('randomNumber2')
        logStuffTitle.append('epsilon')
        logStuffTitle.append('a')
        logStuffTitle.append('r')
        logStuffTitle.append('W')
        logStuff.append(logStuffTitle)
        
        Ws = []
        R_avg = 0.0
        pr = 0
        ql = 0
        for episode in range(self.K):
            # Assign to each policy the probability of being selected
            P = self.assignProbsToPolicies(W, self.tau)

            P[0] = 0.25
            P[1] = 0.75

            # Choose an action policy PI_k
            k = self.choosePolicy(P)

            # Execute the learning episode k
            # Receive R and the updated Q function (Q_omega)
            if k == 0:
                # If PI_k == PI_omega then execute QLearning
                # We are going to dump Ws_dump because the QLearning
                # algorithm runs only once, therefore the returned Ws
                # contains only the R itself (appended below in Ws[])
                R, Ws_dump = myQLearning.execute()
                ql += 1
            else:
                # Else, use the pi-reuse strategy to reuse PI_k
                # chamar funcao pi_reuse()
                Pi_past = L[k]
                R = self.pi_reuse(Pi_past, 1, self.H, self.psi, self.v, logStuff, Q_omega)
                pr += 1

            W[k] = ( (W[k] * U[k]) + R ) / ( U[k] + 1 )
            U[k] = U[k] + 1
            
            self.myQLearning.epsilon = self.myQLearning.epsilon + \
                                       self.myQLearning.epsilonIncrement

            self.tau = self.tau + self.deltaTau

            R_avg = ( (R_avg * episode) + R ) / ( episode + 1 )
            Ws.append(R_avg)

        print 'pr: ', pr, 'ql: ', ql

        f=open(self.filePath + '/log.txt', 'w')
        wr = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
        wr.writerows(logStuff)
        f.close()
        
        return W[0], Ws

    def pi_reuse(self,
                 Pi_past,
                 K,
                 H,
                 psi,
                 v,
                 logStuff,
                 Q_pi_new = None):

        Q_pi_new = self.initializeQ_pi_new(Q_pi_new)
        
        randomNumber1 = -1
        randomNumber2 = -1
        epsilon = -1

        W = 0
        numLine = 0
        for k in range(K):
            # Set the initial state, s, randomly
            self.Agent.setInitialState()
            psi = self.psi
            
            for h in range(1, H + 1):
                s = self.Agent.state

                logStuffLine = []
                logStuffLine.append(len(logStuff) + 1)
                logStuffLine.append(s)

                # if a goal state is reached the episode ends
                if s in self.MDP.G: break

                randomNumber1 = random()
                if randomNumber1 <= psi:
                    # With a probability of psi, a = PI_past(s)
                    # a = myAgent.selectBestAction(s, Q_pi_past)
                    a = Pi_past[s]
                else:
                    # With a probability of (1 - psi), a =
                    # epsilon_greedy(PI_new(s))
                    randomNumber2 = random()
                    
                    epsilon = 1 - psi
                    if randomNumber2 <= epsilon:
                        # greedy
                        a = self.Agent.selectBestAction(s, Q_pi_new)
                    else:
                        #random
                        a = self.Agent.selectRandomAction()

                # Execute action
                # Receive the next state s' and reward r_k_h
                s2, r = self.Agent.executeAction(a)

                maxValue = -1.0
                for a2 in self.MDP.A:
                    if Q_pi_new[s2][a2] > maxValue:
                        maxValue = Q_pi_new[s2][a2]

                # Update Q_pi_new(s, a), and therefore, PI_new
                Q_pi_new[s][a] = ((1.0 - self.alpha) * Q_pi_new[s][a]) + \
                                 self.alpha * (r + self.gamma * maxValue)

                # Set psi_(h + 1) = psi_h * v
                psi = psi * v

                # accumulate reward on W
                W = float(W) + pow(self.gamma, h) * r

                # Set s = s'
                self.Agent.state = s2

                # prepare stuff to do the log
                logStuffLine.append(psi)
                logStuffLine.append(float(randomNumber1))
                logStuffLine.append(float(randomNumber2))
                logStuffLine.append(epsilon)
                logStuffLine.append(a)
                logStuffLine.append(r)
                logStuffLine.append(W)
                logStuff.append(logStuffLine)

        # Update W according to the formula
        W = float(W) / float(K)
        
        return W

    def assignProbsToPolicies(self, W, tau):
        n = len(W)
        denominator = 0
        for p in range(n):
            denominator = denominator + exp(tau * W[p])

        P = []
        for j in range(n):
            p = exp(tau * W[j]) / denominator
            P.append(p)

        return P

    def choosePolicy(self, P):
        P = cumsum(P)
        randomNumber = random()
        k = 0
        for i in range(len(P)):
            if randomNumber <= P[i]:
                k = i
                break
        return k

    def initializeQ_omegaWU(self):
        myMDP = self.MDP
        Q_omega = {}
        S = myMDP.S
        A = myMDP.A
        for s in S:
            Q_omega[s] = {}
            for a in A:
                Q_omega[s][a] = 0.0

        W = []
        U = []
        n = len(self.L)
        for i in range(n):
            W.append(0.0)
            U.append(0)

        return Q_omega, W, U

    def loadPolicies(self):
        policiesPath = self.filePath + '/policies'
        dirList = listdir(policiesPath)

        L = []
        for policyFile in dirList:
            Pi = self.loadPolicy(policiesPath + '/' + policyFile)
            L.append(Pi)

        # free the first position in the library: put the policy
        # that is current there after the last one
        # 
        # Note: the first position is used to store the policy
        #       that is being learned by the PRQL algorithm
        L.append(L[0])
        L[0] = None

        return L
    
    def loadPolicy(self, filePath):
        Pi = {}

        f = open(filePath, 'r')
        for line in f:
            s, a = line.rstrip('\n').split(' ')
            Pi[s] = a
        f.close()

        return Pi

    def initializeQLearning(self, Q = None):
        myQLearning = QLearning.QLearning(self.MDP,                 \
                                          self.Agent,               \
                                          self.alpha,               \
                                          self.gamma,               \
                                          self.epsilon,             \
                                          self.epsilonIncrement,    \
                                          1,                        \
                                          self.H,                   \
                                          Q          = Q,           \
                                          gammaPRQL  = self.gammaPRQL)

        return myQLearning

    def initializeQ_pi_new(self, Q_pi_new):
        if Q_pi_new == None:
            # Initialize Q_pi_new
            # user didn't provide a table: will have to create one
            # For each state-action pair (s, a), initialize the table entry Q(s, a) to zero
            Q_pi_new = {}
            for s in S:
                Q_pi_new[s] = {}
                for a in A:
                    Q_pi_new[s][a] = 0.0

        return Q_pi_new
