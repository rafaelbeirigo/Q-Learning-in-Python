#!/usr/bin/env python
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
                  G = None):
        self.S = S
        self.A = A
        self.T = T
        self.R = R
        self.G = G #final (goal) states

    def carrega(self, filePath):
        caminho = '/home/rafaelbeirigo/Dropbox/IC-Rafael/QLearning/python'

        ##########
        # States #
        ##########
        f = open(filePath + '/states.in')
        S = []
        for line in f:
            S.append(line.strip())

        f.close()

        ###########
        # Actions #
        ###########
        f = open(filePath + '/actions.in')
        A = []
        for line in f:
            A.append(line.strip())

        f.close()

        ###############
        # Transitions #
        ###############
        #create the hash map with initial values equal to zero
        T = {}
        for s in S:
            T[s] = {}
            for a in A:
                T[s][a] = {}
                for s2 in S:
                    T[s][a][s2] = 0.0

        #read transitions from file
        f = open(filePath + '/transitions.in')
        for line in f:
            s, a, s2, t = line.rstrip('\n').split(' ')
            T[s][a][s2] = float(t)

        f.close()

        ###########
        # Rewards #
        ###########
        #create the hash map with initial values equal to zero
        R = {}
        for s in S:
            R[s] = {}
            for a in A:
                R[s][a] = 0.0

        #atualizar os valores das recompensas de acordo com o informado
        #no arquivo
        f = open(filePath + '/rewards.in')
        for line in f:
            s, a, r = line.rstrip('\n').split(' ')
            R[s][a] = float(r)

        f.close()

        self.S = S
        self.A = A
        self.T = T
        self.R = R
        
        #########
        # Goals #
        #########
        f = open(filePath + '/goals.in')
        G = []
        for line in f:
            G.append(line.strip())

        f.close()

        self.S = S
        self.A = A
        self.T = T
        self.R = R
        self.G = G

        return S, A, T, R, G

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

    def isFinalState(self, s):
        return s in self.G
