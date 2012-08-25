#!/usr/bin/env python2

# This is going to be one of the learning algorithms that I will use
# Well, I have then the choice given by the modularity
import operator

class QabLearning:
    def __init__(self, MDP = None, Agent = None, alpha = None, gamma = None, episodes = None, Qab = None, V_star = None):
        self.MDP = MDP
        self.Agent = Agent
        #Learning parameters
        self.alpha = alpha
        self.gamma = gamma
        self.episodes = episodes
        self.Qab = Qab
        self.V_star = V_star
        
    def execute(self):
        myAgent = self.Agent
        myMDP = self.MDP
        a = None
        
        # For each state-action pair (s, a), initialize the table entry Qab(s, a) to zero
        Qab = {}
        S = myMDP.S
        A = myMDP.A
        for s in S:
            Qab[s] = {}
            for a in A:
                Qab[s][a] = 0

        # Observe the current state s
        s2 = myAgent.state
        for i in range(5000):
            # Do forever:
            # ---Select an action  a and execute it
            # ---Receive immediate reward r
            # ---Observe the new state s
            a = myAgent.selectAction()
            s2, r = myAgent.executeAction(a)

            # ---Update the table entry for Qab(s, a) as follows:
            # Qab(s, a) = r * gamma * max_a' Qab (s', a')

            #testar se max funciona com dictionaries
            #Qab[s][a] = r * self.gamma * max(Qab[s2])
            s = myAgent.state
            alpha = self.alpha
            gamma = self.gamma
            Qab[s][a] = (1 - alpha) * float(Qab[s][a]) + (alpha) * (float(r) + gamma * float(max(Qab[s2].values())))

            # ---s=s'
            myAgent.state = s2

            if myMDP.isFinalState(myAgent.state):
                myAgent.setInitialState()
                
        self.Qab = Qab

    def obtainV_star(self):
        #percorrer Qab, obtendo, para cada estado, a acao que fornece o maior valor
        S = self.MDP.S
        V = {}
        for s in S:
            argMax = max(self.Qab[s].iteritems(), key=operator.itemgetter(1))[0]
            V[s] = argMax

        self.V_star = V
