#!/bin/bash

ALGORITHM=$1
PREFIX=$2
SUFFIX=$3
START=$4
END=$5
COMMANDPATH=$6

until [ $START -gt $END ]; do
    echo '/home/'$START
    ./RL-$ALGORITHM.py --filePath=$PREFIX$/START/$SUFFIX/ \
                       --commandPath=$COMMANDPATH \
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
                 > $PREFIX$/START/$SUFFIX/shell.out &
    let START+=1
done