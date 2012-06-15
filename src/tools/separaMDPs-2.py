# Resolve os arquivos enviados pelo Marcelo com os experimentos
# para rodar

import os
import shutil
import glob

goals = [17, 20, 23, 26, 29, 92, 95, 101, 104, 125, 131, 137, 148]
goals.sort()

strategies = ['ipmu', 'manu', 'QL']

mdpFiles = ['states', 'actions', 'transitions', 'rewards']

dirRaiz = '/home/rafaelbeirigo/ql/experiments/174/'

numExperiment = 1
for goal in goals:
    dirExperiment = os.path.join(dirRaiz, str(numExperiment))
    os.mkdir(dirExperiment)
    
    # cria as pastas necessarias
    for strategie in strategies:
        dirStrategie = os.path.join(dirExperiment, strategie)
        os.mkdir(dirStrategie)
        
        # copia os arquivos do MDP para as pastas criadas
        # goals.in
        shutil.copy(os.path.join(dirRaiz, 'goals.in'), dirStrategie)
    
        # S, A, T, R
        for mdpFile in mdpFiles:
            shutil.copy(os.path.join(dirRaiz, 'mdp-' + str(goal) + '-' + mdpFile + '.in'),
                        os.path.join(dirStrategie, mdpFile + '.in'))

        dirPolicies = os.path.join(dirStrategie, 'policies')
        os.mkdir(dirPolicies)

        # copia policies
        policyFiles = glob.glob(os.path.join(dirRaiz, 'pi-' + strategie + '-' + str(goal) + '*'))
        print policyFiles
        
        for policyFile in policyFiles:
            shutil.copy(os.path.join(dirRaiz, policyFile),
                        dirPolicies)

    numExperiment += 1
