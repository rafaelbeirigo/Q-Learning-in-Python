#!/usr/bin/env python

import QLearning
import operator
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

        L[0] = Q_omega

        myQLearning = self.initializeQLearning()
        self.myQLearning = myQLearning

        Ws = []
        R_avg = 0.0
        pr = 0
        ql = 0
        for episode in range(self.K):
            # Assign to each policy the probability of being selected
            P = self.assignProbsToPolicies(W, self.tau)

            # Choose an action policy PI_k
            k = self.choosePolicy(P)

            # Execute the learning episode k
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
                Q_pi_past = L[k]
                R = self.pi_reuse(Q_pi_past, 1, self.H, self.psi, self.v, Q_omega)
                pr += 1

            # Receive R and the updated Q function (Q_omega)
            W[k] = ( (W[k] * U[k]) + R ) / ( float(U[k] + 1) )
            U[k] = U[k] + 1
            self.tau = self.tau + self.deltaTau

            self.myQLearning.epsilon = self.myQLearning.epsilon + \
                                       self.myQLearning.epsilonIncrement

            R_avg = ( (R_avg * episode) + R ) / ( episode + 1 )
            Ws.append(R_avg)

        print 'pr: ', pr, 'ql: ', ql
        
        return W[0], Ws

    def pi_reuse(self,
                 Q_pi_past,
                 K,
                 H,
                 psi,
                 v,
                 Q_pi_new = None):

        S = self.MDP.S
        A = self.MDP.A

        if Q_pi_new == None:
            # Initialize Q_pi_new
            # user didn't provide a table: will have to create one
            # For each state-action pair (s, a), initialize the table entry Q(s, a) to zero
            Q_pi_new = {}
            for s in S:
                Q_pi_new[s] = {}
                for a in A:
                    Q_pi_new[s][a] = 0.0

        alpha            = self.alpha
        gamma            = self.gamma
        epsilon          = self.epsilon
        epsilonIncrement = self.epsilonIncrement
        psi2             = self.psi
        
        W = 0
        for k in range(K):
            # Set the initial state, s, randomly
            self.Agent.setInitialState()

            for h in range(1, H + 1):
                s = self.Agent.state

                # if a goal state is reached the episode ends
                if s in self.MDP.G: break

                randomNumber1 = random()
                if randomNumber1 <= psi2:
                    # With a probability of psi, a = PI_past(s)
                    # a = myAgent.selectBestAction(s, Q_pi_past)
                    a = Q_pi_past[s]
                else:
                    # With a probability of (1 - psi), a = 
                    # epsilon_greedy(PI_new(s))
                    
                    randomNumber2 = random()
                    epsilon = 1 - psi2
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
                for a2 in A:
                    if Q_pi_new[s2][a2] > maxValue:
                        maxValue = Q_pi_new[s2][a2]

                # Update Q_pi_new(s, a), and therefore, PI_new
                Q_pi_new[s][a] = (1.0 - float(alpha)) * float(Q_pi_new[s][a]) + \
                                 float(alpha) * (float(r) + float(gamma) * float(maxValue))

                # Set psi_(h + 1) = psi_h * v
                psi2 = psi2 * v

                # accumulate reward on W
                W = float(W) + pow(gamma, h) * r

                # Set s = s'
                self.Agent.state = s2

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

    def initializeQLearning(self):
        myQLearning = QLearning.QLearning(self.MDP,                 \
                                          self.Agent,               \
                                          self.alpha,               \
                                          self.gamma,               \
                                          self.epsilon,             \
                                          self.epsilonIncrement,    \
                                          1,                        \
                                          self.H,                   \
                                          Q          = self.L[0],   \
                                          gammaPRQL  = self.gammaPRQL)

        return myQLearning
