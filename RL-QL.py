#!/usr/bin/env python

# o que precisa fazer pra rodar o aprendizado
# instanciar classes
import MDP
import Agent
import QLearning
import time

def main():
    myMDP = MDP.MDP()
    myMDP.carrega('/home/rafaelbeirigo/Dropbox/IC-Rafael/QLearning/python/problems/WTA/19/')

    myAgent = Agent.Agent(myMDP)
    myAgent.setInitialState()
    
    alpha = 0.9
    gamma = 0.9
    episodes = 1000
    myQLearning = QLearning.QLearning(myMDP, myAgent, alpha, gamma, episodes)
    myQLearning.execute()
    myQLearning.obtainV_star()
    
    print myQLearning.Q
    print myQLearning.V_star
main()
