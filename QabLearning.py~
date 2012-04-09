#!/usr/bin/env python

# This is going to be one of the learning algorithms that I will use
# Well, I have then the choice given by the modularity
import operator

class QLearning:
    def __init__(self, MDP = None, Agent = None, alpha = None, gamma = None, episodes = None, Q = None, V_star = None):
        self.MDP = MDP
        self.Agent = Agent
        #Learning parameters
        self.alpha = alpha
        self.gamma = gamma
        self.episodes = episodes
        self.Q = Q
        self.V_star = V_star
        
    def execute(self):
        myAgent = self.Agent
        myMDP = self.MDP
        a = None
        
        # For each state-action pair (s, a), initialize the table entry Q(s, a) to zero
        Q = {}
        S = myMDP.S
        A = myMDP.A
        for s in S:
            Q[s] = {}
            for a in A:
                Q[s][a] = 0

        # Observe the current state s
        s2 = myAgent.state
        for i in range(5000):
            # Do forever:
            # ---Select an action  a and execute it
            # ---Receive immediate reward r
            # ---Observe the new state s
            a = myAgent.selectAction()
            s2, r = myAgent.executeAction(a)

            # ---Update the table entry for Q(s, a) as follows:
            # Q(s, a) = r * gamma * max_a' Q (s', a')

            #testar se max funciona com dictionaries
            #Q[s][a] = r * self.gamma * max(Q[s2])
            s = myAgent.state
            alpha = self.alpha
            gamma = self.gamma
            Q[s][a] = (1 - alpha) * float(Q[s][a]) + (alpha) * (float(r) + gamma * float(max(Q[s2].values())))

            # ---s=s'
            myAgent.state = s2

            if myMDP.isFinalState(myAgent.state):
                myAgent.setInitialState()
                
        self.Q = Q

    def obtainV_star(self):
        #percorrer Q, obtendo, para cada estado, a acao que fornece o maior valor
        S = self.MDP.S
        V = {}
        for s in S:
            argMax = max(self.Q[s].iteritems(), key=operator.itemgetter(1))[0]
            V[s] = argMax

        self.V_star = V
