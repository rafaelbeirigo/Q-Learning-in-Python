#!/usr/bin/env python
from Agent import Agent
from MDP import MDP
from QLearning import QLearning
from prepareFolders import prepareFolders
import time
import sys
from pylab import array
import getopt

def usage():
    print 'Soon there will be a help message here.'

def obtainParameters():
    try:
        optNames = ['filePath=', \
                    'commandPath=', \
                    'alpha=', \
                    'gamma=', \
                    'epsilon=', \
                    'epsilonIncrement=', \
                    'gammaPRQL=', \
                    'K=', \
                    'H=', \
                    'numberOfExecutions=']

        if len(sys.argv[1:]) != len(optNames):
            print 'error: please inform the parameters correctly'
            sys.exit(1)

        opts, args = getopt.getopt(sys.argv[1:], "", optNames)
    except getopt.GetoptError, err:
        usage()
        print str(err) # will print something like "option -a not recognized"
        sys.exit(2)

    params = {}
    for optName in optNames:
        params[optName[:-1]] = None
        
    for opt, arg in opts:
        # The first two characters are '--', therefore, they are ignored
        params[opt[2:]] = arg

        if opt in ("-h", "--help"):
            usage()
            sys.exit()

    return params

def saveOutputFiles(myQLearning, params, Ws):
    filePath = params['filePath']
    myQLearning.obtainPolicy()
    myQLearning.printPolicy(filePath + 'policy.out')
    myQLearning.printQ(filePath + 'Q.out')

    f = open(filePath + 'parameters.out', 'w')
    f.write('alpha              = ' + params['alpha']              + '\n')
    f.write('gamma              = ' + params['gamma']              + '\n')
    f.write('epsilon            = ' + params['epsilon']            + '\n')
    f.write('epsilonIncrement   = ' + params['epsilonIncrement']   + '\n')
    f.write('K                  = ' + params['K']                  + '\n')
    f.write('H                  = ' + params['H']                  + '\n')
    f.write('numberOfExecutions = ' + params['numberOfExecutions'] + '\n')
    f.close()

    f = open(filePath + 'w.out', 'w')
    for w in Ws:
        f.write(str(w) + '\n')
    f.close()


def main():
    # resolve the parameters sent from the command line call
    params = obtainParameters()

    # resolve file issues regarding the execution of the algorithm
    prepareFolders(params['commandPath'], params['filePath'])

    myMDP = MDP(params['filePath'])
    myAgent = Agent(myMDP)

    Wacumulado = 0
    for i in range(int(params['numberOfExecutions'])):
        print 'Running experiment ' + str(i + 1) + ' of ' + str(params['numberOfExecutions'])

        myQLearning = QLearning(myMDP,                                                \
                                myAgent,                                              \
                                alpha            = float(params['alpha']),            \
                                gamma            = float(params['gamma']),            \
                                epsilon          = float(params['epsilon']),          \
                                epsilonIncrement = float(params['epsilonIncrement']), \
                                K                = int(params['K']),                  \
                                H                = int(params['H']),                  \
                                gammaPRQL        = float(params['gammaPRQL']))

        W, Ws = myQLearning.execute()
        Wacumulado += array(Ws)
        
    Ws = Wacumulado / float(params['numberOfExecutions'])

    saveOutputFiles(myQLearning, params, Ws)
    
if __name__ == "__main__":
    main()

# ./RL-QL.py --filePath='/home/rafaelbeirigo/ql/experiments/tests/QL/' --commandPath='/home/rafaelbeirigo/ql/tools/' --alpha=0.05 --gamma=0.95 --gammaPRQL=0.95 --epsilon=0.0 --epsilonIncrement=0.0005 --K=2000 --H=100 --numberOfExecutions=1000

# old list of standard parameters:
#    alpha              = 0.05
#    gamma              = 0.95
#    epsilon            = 0.0
#    epsilonIncrement   = 0.0005
#    gammaPRQL          = 0.95
#    K                  = 2000       # number of episodes
#    H                  = 100        # number of steps
#    numberOfExecutions = 1000
