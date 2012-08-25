#!/bin/bash

PREFIX=$1
SUFFIX=$2
START=$3
END=$4
COMMANDPATH=$5
K=$6
H=$7

echo PREFIX:$PREFIX SUFFIX:$SUFFIX START:$START END:$END COMMANDPATH:$COMMANDPATH K:$K H:$H

if [[ -z "$PREFIX" || -z "$SUFFIX" || -z "$START" || -z "$END" || -z "$COMMANDPATH" || -z "$K" || -z "$H" ]]
then
    echo usage: QL-interval.sh [PREFIX] [SUFFIX] [START] [END] [COMMANDPATH] [K] [H]
    exit
fi

until [ $START -gt $END ]; do
    ./RL-QL.py --filePath=$PREFIX/$START/$SUFFIX/ \
               --commandPath=$COMMANDPATH/ \
               --alpha=0.05 \
               --gamma=0.95 \
               --epsilon=0.05 \
               --epsilonIncrement=0.0 \
               --gammaPRQL=0.95 \
               --K=$K \
               --H=$H \
               --numberOfExecutions=10
    
    let START+=1
done
