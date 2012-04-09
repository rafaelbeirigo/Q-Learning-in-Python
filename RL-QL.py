#!/usr/bin/env python

import MDP
import Agent
import QLearning
import time
import sys
import pylab as pl

def main():
    filePath = sys.argv[1]
    myMDP = MDP.MDP()
    myMDP.carrega(filePath)

    myAgent = Agent.Agent(myMDP)
    
    alpha              = 0.05
    gamma              = 0.95
    epsilon            = 0.0
    epsilonIncrement   = 0.0005
    gammaPRQL          = 0.95

    K                  = 2000       # number of episodes
    H                  = 100        # number of steps
    numberOfExecutions = 10

    Wacumulado = 0
    for i in range(numberOfExecutions):
        print 'Running experiment ' + str(i + 1) + ' of ' + str(numberOfExecutions)
        myQLearning = None
        myQLearning = QLearning.QLearning(myMDP,                               \
                                          myAgent,                             \
                                          alpha            = alpha,            \
                                          gamma            = gamma,            \
                                          epsilon          = epsilon,          \
                                          epsilonIncrement = epsilonIncrement, \
                                          K                = K,                \
                                          H                = H,                \
                                          gammaPRQL        = gammaPRQL)

        W, Ws = myQLearning.execute()
        Wacumulado += pl.array(Ws)
        
    Ws = Wacumulado / numberOfExecutions

    myQLearning.obtainPolicy()
    myQLearning.printPolicy(filePath + 'policy.out')
    myQLearning.printQ(filePath + 'Q.out')

    f = open(filePath + 'parameters.out', 'w')
    f.write('alpha            = ' + str(alpha) + '\n')
    f.write('gamma            = ' + str(gamma) + '\n')
    f.write('epsilon          = ' + str(epsilon) + '\n')
    f.write('epsilonIncrement = ' + str(epsilonIncrement) + '\n')
    f.write('K                = ' + str(K) + '\n')
    f.write('H                = ' + str(H) + '\n')
    f.write('gammaPRQL        = ' + str(gammaPRQL) + '\n')
    f.close()

    f = open(filePath + 'w.out', 'w')
    for w in Ws:
        f.write(str(w) + '\n')
    f.close()

    #pl.plot(range(len(Ws)), Ws)
    #pl.savefig(filePath + 'graph')
    #pl.plot(range(len(Ws)), Ws)
    #pl.show()
    
main()
