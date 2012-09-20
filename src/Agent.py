#!/usr/bin/env python2
import random

class Agent:
    def __init__(self, MDP):
        self.MDP = MDP
        self.state = None

    def executeAction(self, a):
        s2, r = self.MDP.executeAction(a, self.state)
        return s2, r

    def selectRandomAction(self):
        return random.choice(self.MDP.A_s[self.state])

    def selectBestActionFromQTable(self, s, Q):
        # discover what is the best possible value considering
        # all possible actions for the state

        # FIXME: usar a tabela V
        maxValue = 0.0
        for a in self.MDP.A_s[self.state]:
            maxValue = max(maxValue, Q[s][a])

        # obtain all the actions whose value equals the maximum
        A = []
        for a in self.MDP.A_s[self.state]:
            # FIXME: make it a parameter
            delta = 1e-10
            if abs(Q[s][a] - maxValue) <= delta:
                A.append(a)

        # obtain a random action from all the possible ones
        if len(A) > 0:
            a = random.choice(A)
        else:
            a = '---'

        return a

    def selectBestActionFromProbPolicy(self, s, Pi):
        P = []
        acum = 0.0

        # FIXME: eliminar a necessidade de ter que rodar a soma
        # cumulativa a toda chamada
        #
        # Fazer essa checagem na leitura da politica agregar uma lista
        # de pares ordenados ja com a probabilidade acumulada.
        # Sortear e somente buscar na lista ate encontrar a acao da
        # vez.
        #
        # PROBLEMA: a politica pode mudar!  Alternativa: mudar a forma
        # como a politica e carregada: Fazer chegar aqui ja uma Pi[s]
        # = [(action, cumsum)]
        
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
        x = random.random()

        for p in self.MDP.P:
            if x <= p[1]:
                s = p[0]
                break

        return s
