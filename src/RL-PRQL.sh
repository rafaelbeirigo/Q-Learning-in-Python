#!/bin/bash

ALGORITHM=$1
PREFIX=$2
SUFFIX=$3
START=$4
END=$5
COMMANDPATH=$6
K=$7
H=$8

echo ALGORITHM:$ALGORITHM PREFIX:$PREFIX SUFFIX:$SUFFIX START:$START END:$END COMMANDPATH:$COMMANDPATH K:$K H:$H

if [[ -z "$ALGORITHM" || -z "$PREFIX" || -z "$SUFFIX" || -z "$START" || -z "$END" || -z "$COMMANDPATH" || -z "$K" || -z "$H" ]]
then
    echo usage: RL-PRQL.sh [ALGORITHM] [PREFIX] [SUFFIX] [START] [END] [COMMANDPATH] [K] [H]
    exit
fi

until [ $START -gt $END ]; do
    ./RL-$ALGORITHM.py --filePath=$PREFIX/$START/$SUFFIX/ \
                       --commandPath=$COMMANDPATH/ \
                       --alpha=0.05 \
                       --gamma=0.95 \
                       --epsilon=1.0 \
                       --epsilonIncrement=0.0 \
                       --gammaPRQL=0.95 \
                       --K=$K \
                       --H=$H \
                       --numberOfExecutions=10 \
                       --tau=0.0 \
                       --deltaTau=0.05 \
                       --psi=1.0 \
                       --v=0.95
    
    let START+=1
done
