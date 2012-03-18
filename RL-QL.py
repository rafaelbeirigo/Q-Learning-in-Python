#!/usr/bin/env python

# o que precisa fazer pra rodar o aprendizado
# instanciar classes
import MDP
import Agent
import QLearning
import time
import sys

def main():
    myMDP = MDP.MDP()
    myMDP.carrega(sys.argv[1])

    myAgent = Agent.Agent(myMDP)
    myAgent.setInitialState()
    
    alpha =            0.75
    gamma =            0.9
    epsilon =          0.0
    epsilonIncrement = 0.000099
    numberOfSteps =     100000
    
    myQLearning = QLearning.QLearning(myMDP, myAgent, \
                                      alpha = alpha, \
                                      gamma = gamma, \
                                      epsilon = epsilon, \
                                      epsilonIncrement = epsilonIncrement, \
                                      numberOfSteps = numberOfSteps)

    myQLearning.execute()
    myQLearning.obtainPolicy()

    myQLearning.printPolicy(sys.argv[1] + 'policy.out')
    myQLearning.printQ(sys.argv[1] + 'Q.out')

    f = open(sys.argv[1] + 'parameters.out', 'w')
    f.write('alpha =            ' + str(alpha) + '\n')
    f.write('gamma =            ' + str(gamma) + '\n')
    f.write('epsilon =          ' + str(epsilon) + '\n')
    f.write('epsilonIncrement = ' + str(epsilonIncrement) + '\n')
    f.write('numberOfSteps =    ' + str(numberOfSteps) + '\n')
    f.close()
main()
