#!/usr/bin/env python2
from Agent import Agent
from MDP import MDP
from PRQLearning import PRQLearning
from prepareFolders import prepareFolders
import time
import sys
from pylab import array
import getopt
import numpy as np
import meanError

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
                    'numberOfExecutions=', \
                    'tau=', \
                    'deltaTau=', \
                    'psi=', \
                    'v=']

        if len(sys.argv[1:]) != len(optNames):
            print 'error: please inform the parameters correctly'
            print len(optNames), len(sys.argv[1:])
            print sys.argv[1:]
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

def accumulateOutput(outputAccum, output):
    if not outputAccum:
        # dictionary outputAccum is empty
        for name in output.iterkeys():
            outputAccum[name] = []
            
    for name in output.iterkeys():
        outputAccum[name].append(output[name])

def saveOutputFiles(myQLearning, params, output):
    filePath = params['filePath']
    myQLearning.obtainPolicy()
    myQLearning.printPolicy(filePath + 'policy.out')
    myQLearning.printQ(filePath + 'Q.out')

    f = open(filePath + 'parameters.out', 'w')
    f.write('alpha              = ' + params['alpha']              + '\n')
    f.write('gamma              = ' + params['gamma']              + '\n')
    f.write('epsilon            = ' + params['epsilon']            + '\n')
    f.write('epsilonIncrement   = ' + params['epsilonIncrement']   + '\n')
    f.write('gammaPRQL          = ' + params['gammaPRQL']          + '\n')
    f.write('tau                = ' + params['tau']                + '\n')
    f.write('deltaTau           = ' + params['deltaTau']           + '\n')
    f.write('psi                = ' + params['psi']                + '\n')
    f.write('v                  = ' + params['v']                  + '\n')
    f.write('K                  = ' + params['K']                  + '\n')
    f.write('H                  = ' + params['H']                  + '\n')
    f.write('numberOfExecutions = ' + params['numberOfExecutions'] + '\n')
    f.close()

    #names = ['Ps']
    for name in output.iterkeys():
        #if name not in names: continue
        print name
        d = output[name]
        if len(d) > 1:
            dMean = meanError.meanMultiDim(d)
            dCfdInt = meanError.confidenceIntervalMultiDim(d, dMean)

            dMean = np.asarray(dMean)
            dCfdInt = np.asarray(dCfdInt)

            dMean.T
            dCfdInt.T

            np.savetxt(filePath + '/' + name + '_mean.out', dMean)
            np.savetxt(filePath + '/' + name + '_cfdInt.out', dCfdInt)
        else:
            d = np.asarray(d)
            d.T
            np.savetxt(filePath + '/' + name + '.out', d)

def main():
    # resolve the parameters sent from the command line call
    params = obtainParameters()

    # resolve file issues regarding the execution of the algorithm
    prepareFolders(params['commandPath'], params['filePath'])

    myMDP = MDP(params['filePath'])
    myAgent = Agent(myMDP)
    
    W_avg_list_accum = 0
    outputAccum = {}
    for i in range(int(params['numberOfExecutions'])):
        print 'Running experiment ' + str(i + 1) + ' of ' + str(params['numberOfExecutions']); sys.stdout.flush()

        myPRQLearning = PRQLearning(myMDP,                                                \
                                    myAgent,                                              \
                                    alpha            = float(params['alpha']),            \
                                    gamma            = float(params['gamma']),            \
                                    epsilon          = float(params['epsilon']),          \
                                    epsilonIncrement = float(params['epsilonIncrement']), \
                                    K                = int(params['K']),                  \
                                    H                = int(params['H']),                  \
                                    gammaPRQL        = float(params['gammaPRQL']),        \
                                    tau              = float(params['tau']),              \
                                    deltaTau         = float(params['deltaTau']),         \
                                    psi              = float(params['psi']),              \
                                    v                = float(params['v']),                \
                                    filePath         = params['filePath'])

        output = myPRQLearning.execute()
        accumulateOutput(outputAccum, output)

        W_avg_list = output['W_avg_list']
        W_avg_list_accum += array(W_avg_list)

    W_avg_list = W_avg_list_accum / float(params['numberOfExecutions'])
    saveOutputFiles(myPRQLearning.myQLearning, params, outputAccum)

if __name__ == "__main__":
    main()

# ./RL-PRQL.py --filePath='/home/rafaelbeirigo/ql/experiments/tests/PRQL/' --commandPath='/home/rafaelbeirigo/ql/tools/' --alpha=0.05 --gamma=0.95 --epsilon=1.0 --epsilonIncrement=0.0000 --gammaPRQL=0.95 --tau=0.0 --deltaTau=0.05 --psi=1.0 --v=0.95 --K=2000 --H=100 --numberOfExecutions=1000


# old list of standard parameters:
#    alpha              = 0.05
#    gamma              = 0.95
#    epsilon            = 1.0
#    epsilonIncrement   = 0.0000
#    gammaPRQL          = 0.95
#    tau                = 0.0
#    deltaTau           = 0.05
#    psi                = 1.0
#    v                  = 0.95
#    K                  = 2000     # number of episodes
#    H                  = 100      # number of steps
#    numberOfExecutions = 1000
