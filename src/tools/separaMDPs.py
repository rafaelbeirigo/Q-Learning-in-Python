## Resolve arquivos do MDP
## faz uma pasta para cada experimento


## Resolve arquivos de politicas abs-prob
## entra na pasta

## pega o arquivo

## descobre o numero do experimento

## coloca na pasta do experimento

## a regra é todo mundo com esse número de experimento vai pra pasta


## # resolve arquivos de politicas manu1
## para cada pasta de experimento
##     para cada arquivo de manu1 arqExp
##         descobre o experimento do arquivo
##             se experimento do arquivo é DIFERENTE do experimento da pasta
##                 copia o arquivo para a pasta do experimento


## # resolve arquivos de politicas manu2 e absprob
## mesma coisa do manu2

import os
import shutil

goals = [17, 20, 23, 26, 29, 62, 74, 107, 110, 113, 119, 701]
goals.sort()

dirRaiz = '/home/rafaelbeirigo/ql/experiments/lalala/'
dirMDP = dirRaiz + '/mdps/'

numExperiment = 1
dirPol = dirRaiz + '/politicas-absprob/'
for goal in goals:
    # cria as pastas necessárias
    dirExperiment = os.path.join(dirRaiz, str(numExperiment))
    dirPRQL = os.path.join(dirExperiment, 'PRQL')
    dirPolicies = os.path.join(dirPRQL, 'policies')

    dirs = [dirExperiment, dirPRQL, dirPolicies]
    for d in dirs: os.mkdir(d)

    # copia o arq. de goals (igual para todos os exper.)
    shutil.copy(os.path.join(dirRaiz, 'goals.in'), dirPRQL)
    
    # arquivos do MDP
    for fileName in os.listdir(dirMDP):
        fileGoal = int(str.split(fileName, '-')[1])
        fileNameDest = str.split(fileName, '-')[2]
        if fileGoal == goal:
            # copia o arquivo para a pasta do experimento
            shutil.copy(os.path.join(dirMDP, fileName),
                        os.path.join(dirPRQL, fileNameDest))
    # arquivos de politicas
    for fileName in os.listdir(dirPol):
        fileGoal = int(str.split(fileName, '-')[3])
        fileNameDest = fileName + '.in'
        if fileGoal == goal:
            # copia o arquivo para a pasta do experimento
            shutil.copy(os.path.join(dirPol, fileName),
                        os.path.join(dirPolicies, fileNameDest))

    numExperiment += 1

dirPols = [dirRaiz + '/politicas-manu1/',
           dirRaiz + '/politicas-manu2/']
for dirPol in dirPols:
    for goal in goals:
        # cria as pastas necessárias
        dirExperiment = os.path.join(dirRaiz, str(numExperiment))
        dirPRQL = os.path.join(dirExperiment, 'PRQL')
        dirPolicies = os.path.join(dirPRQL, 'policies')

        dirs = [dirExperiment, dirPRQL, dirPolicies]
        for d in dirs: os.mkdir(d)

        # copia o arq. de goals (igual para todos os exper.)
        shutil.copy(os.path.join(dirRaiz, 'goals.in'), dirPRQL)

        # arquivos do MDP
        for fileName in os.listdir(dirMDP):
            fileGoal = int(str.split(fileName, '-')[1])
            fileNameDest = str.split(fileName, '-')[2]
            if fileGoal == goal:
                # copia o arquivo para a pasta do experimento
                shutil.copy(os.path.join(dirMDP, fileName),
                            os.path.join(dirPRQL, fileNameDest))
        # arquivos de politicas
        for fileName in os.listdir(dirPol):
            print fileName
            fileGoal = int(str.split(fileName, '-')[1])
            fileNameDest = fileName + '.in'
            if fileGoal != goal:
                # copia o arquivo para a pasta do experimento
                shutil.copy(os.path.join(dirPol, fileName),
                            os.path.join(dirPolicies, fileNameDest))

        numExperiment += 1
