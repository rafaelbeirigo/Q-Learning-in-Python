#!/usr/bin/env python
import os.path
import Agent
import string
import random

class MDP:
    # filePath e o caminho para a pasta que contem os arquivos de configuracao
    def __init__ (self, 
                  S = None, 
                  A = None, 
                  T = None, 
                  R = None, 
                  G = None,
                  P = None):
        self.S = S
        self.A = A
        self.T = T
        self.R = R
        self.G = G
        self.P = P

    def carrega(self, filePath):
        self.S = self.loadStates(filePath)
        self.A = self.loadActions(filePath)
        self.T = self.loadTransitions(filePath)
        self.R = self.loadRewards(filePath)
        self.G = self.loadGoals(filePath)
        if os.path.exists(filePath + '/initialStateProb.in'):
            self.P = self.loadInitialStateProb(filePath)
        else:
            self.P = None

    def loadStates(self, filePath):
        f = open(filePath + '/states.in')
        S = []
        for line in f:
            S.append(line.strip())

        f.close()

        return S

    def loadActions(self, filePath):
        f = open(filePath + '/actions.in')
        A = []
        for line in f:
            A.append(line.strip())

        f.close()

        return A
        
    def loadTransitions(self, filePath):
        #create the hash map with initial values equal to zero
        T = {}
        for s in self.S:
            T[s] = {}
            for a in self.A:
                T[s][a] = {}
                for s2 in self.S:
                    T[s][a][s2] = 0.0

        #read transitions from file
        f = open(filePath + '/transitions.in')
        for line in f:
            s, a, s2, t = line.rstrip('\n').split(' ')
            T[s][a][s2] = float(t)

        f.close()

        return T

    def loadRewards(self, filePath):
        #create the hash map with initial values equal to zero
        R = {}
        for s in self.S:
            R[s] = {}
            for a in self.A:
                R[s][a] = 0.0

        #atualizar os valores das recompensas de acordo com o informado
        #no arquivo
        f = open(filePath + '/rewards.in')
        for line in f:
            s, a, r = line.rstrip('\n').split(' ')
            R[s][a] = float(r)

        f.close()

        return R
        
    def loadGoals(self, filePath):
        f = open(filePath + '/goals.in')
        G = []
        for line in f:
            G.append(line.strip())

        f.close()

        return G

    def loadInitialStateProb(self, filePath):
        P = {}
        for s in self.S:
            P[s] = 0.0

        f = open(filePath + '/initialStateProb.in')
        for line in f:
            s, p = line.rstrip('\n').split(' ')
            P[s] = float(p)

        f.close()

        return P

    def isFinalState(self, s):
        return s in self.G
        
    def executeAction(self, a, s):
        T = self.T
        P = []
        acum = 0.0

        for s1 in T[s][a].iterkeys():
            if T[s][a][s1] > 0.0:
                p = []
                p.append(s1)
                acum = acum + T[s][a][s1]
                p.append(acum)
                P.append(p)

        #sorteia um numero no intervalo [0, 1]
        x = random.random()

        #obtem o novo estado s' correspondente ao numero sorteado
        for p in P:
            if x <= p[1]:
                s2 = p[0]
                break

        #obtem a recompensa
        r = self.R[s][a]
        
        return s2, r
