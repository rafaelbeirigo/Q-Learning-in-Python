#!/bin/bash

START=$1
END=$2

#echo $START
#START=START + 1
#echo $START

until [  $START -gt $END ]; do
    echo '/home/'$START
    ./RL-PRQL.py --filePath='/home/rafaelbeirigo/ql/experiments/tests/porcents/eGreedy/'$START'/PRQL/' \
                 --commandPath='/home/rafaelbeirigo/ql/tools/' \
                 --alpha=0.05 \
                 --gamma=0.95 \
                 --epsilon=0.0 \
                 --epsilonIncrement=0.0005 \
                 --gammaPRQL=0.95 \
                 --tau=0.0 \
                 --deltaTau=0.05 \
                 --psi=1.0 \
                 --v=0.95 \
                 --K=2000 \
                 --H=100 \
                 --numberOfExecutions=1000 \
                 > '/home/rafaelbeirigo/ql/experiments/tests/porcents/eGreedy/'$START'/PRQL/shell.out' &
    let START+=1
done