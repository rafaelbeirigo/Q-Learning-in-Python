!/usr/bin/env python

import operator
from math import exp
from random import random
from numpy import cumsum

class PRQLearning:
    def __init__(self,
                 #parameters from article
                 taskOmega = None,
                 policyLibraryL = None,
                 tau = None,
                 deltaTau = None,
                 K = None,
                 H = None,
                 psi = None,
                 v = None,
                 gamma = None, 
                 alpha = None, 
                 
                 #"our" parameters
                 MDP = None, 
                 Agent = None, 
                 Q_omega = None, 
                 V_star = None):

        self.taskOmega = taskOmega
        self.policyLibraryL = policyLibraryL
        self.tau = tau
        self.deltaTau = deltaTau
        self.K = K
        self.H = H
        self.psi = psi
        self.v = v
        self.gamma = gamma
        self.alpha = alpha

        self.MDP = MDP
        self.Agent = Agent
        self.Q_omega = Q_omega
        self.V_star = V_star

    def execute(self):
        myAgent = self.Agent
        myMDP = self.MDP
        
        # Initialize
        # For each state-action pair (s, a), initialize the table entry Q_omega(s, a) to zero
        Q_omega = {}
        S = myMDP.S
        A = myMDP.A
        for s in S:
            Q_omega[s] = {}
            for a in A:
                Q_omega[s][a] = 0

        # The W_omega from the article is W[omega], with omega == 0,
        # and the same applies to U_omega
        omega = 0
        for i in range(n + 1)
            W[i] = 0
            U[i] = 0

        myQLearning = QLearning.QLearning(myMDP, myAgent, self.alpha, self.gamma, K)
                                          MDP = None,
                                          Agent = None,
                                          Q = None,
                                          V_star = None,
                                          alpha = None,
                                          gamma = None,
                                          gammaPRQL = None, #gamma used for PRQLearning algorithm
                                          epsilon = None,
                                          epsilonIncrement = None,
                                          numberOfEpisodes = None):
        
        for i in range(K):
            # Assign to each policy the probability of being selected
            P = assignProbabilities(W, tau, n)4

            # Choose an action policy PI_k
            cumsum(P)
            randomNumber = random()
            for i in range(size(P)):
                if randomNumber <= P[i]:
                    k = i
                    break
            
            # Execute the learning episode k
            if k == 0:
                # If PI_k == PI_omega then execute QLearning
                # TODO: obain return values (including W)
                R = myQLearning.execute()
            else:
                # Else, use the pi-reuse strategy to reuse PI_k
                # chamar função pi_reuse()
                W, Q_pi_new, PI_new = pi_reuse(Q_pi_past, K, H, psi, v, Q_pi_new)

            # Receive R and Q_omega
            # TODO: ver como fica pro QLearning

    def pi_reuse(self,
                 Q_pi_past,
                 K,
                 H,
                 psi,
                 v,
                 Q_pi_new = None):

        if Q_pi_new == None:
            # Initialize Q_pi_new
            # user didn't provide a table: will have to create one
            # For each state-action pair (s, a), initialize the table entry Q(s, a) to zero
            Q_pi_new = {}
            S = self.MDP.S
            A = self.MDP.A
            for s in S:
                Q_pi_new[s] = {}
                for a in A:
                    Q_pi_new[s][a] = 0

        W = 0
        for i in range(K):
            # Set the initial state, s, randomly
            self.Agent.setInitialState()

            s = self.Agent.state
            for h in range(1, H + 1)
                # TODO: encapsular o selecionador de melhor ação em uma
                # classe relacionada a Q-Table
                randomNumber1 = random()
                if randomNumber1 <= psi:
                    # With a probability of psi, a = PI_past(s)
                    a = max(Q_pi_past[s].iteritems(), key=operator.itemgetter(1))[0]
                else:
                    # With a probability of (1 - psi), a = 
                    # epsilon_greedy(PI_new(s))
                    randomNumber2 = random()
                    if randomNumber2 <= epsilon:
                        # greedy
                        a = max(Q_pi_past[s].iteritems(), key=operator.itemgetter(1))[0]
                    else:
                        #random
                        a = self.Agent.selectRandomAction()

                # Execute action
                # Receive the next state s' and reward r_k_h
                r, s2 = self.Agent.executeAction(a)

                # Update Q_pi_new(s, a), 
                # and therefore, PI_new
                Q_pi_new[s][a] = (1 - alpha) * float(Q_pi_new[s][a]) + (alpha) * (float(r) + gamma * float(max(Q_pi_new[s2].values())))

                # Set psi_(h + 1) = psi_h * v
                psi = psi * v

                # Set s = s'
                self.Agent.state = s2

                # accumulate gamma on W
                W = float(W) + pow(gamma, h) * r

        # Update W according to the formula
        W = float(W) / float(K)
        
        return W, Q_pi_new, PI_new

    def assignProbabilities(self,
                            W = None,
                            tau = None,
                            n)

        denominator = 0
        for p in range(n + 1):
            denominator = denominator + exp(tau * W[p])

        P = []
        for j in range(n + 1):
            p = exp(tau * W[j]) / denominator
            P.append(p)

        return P
