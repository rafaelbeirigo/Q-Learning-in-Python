#!/bin/bash

ALGORITHM=$1
PREFIX=$2
SUFFIX=$3
START=$4
END=$5
<<<<<<< HEAD
FILE=$6
NUMLINES=$7

echo ALGORITHM:$ALGORITHM PREFIX:$PREFIX SUFFIX:$SUFFIX START:$START END:$END FILE:$FILE $NUMLINES

if [[ -z "$ALGORITHM" || -z "$PREFIX" || -z "$SUFFIX" || -z "$START" || -z "$END" || -z "$FILE" || -z "$NUMLINES" ]]
then
    echo usage: tailFiles  .sh [ALGORITHM] [PREFIX] [SUFFIX] [START] [END] [FILE] [NUMLINES]
fi

until [ $START -gt $END ]; do
    echo $PREFIX/$START/$SUFFIX/$FILE:
    tail -n $NUMLINES $PREFIX/$START/$SUFFIX/$FILE
=======

echo ALGORITHM:$ALGORITHM PREFIX:$PREFIX SUFFIX:$SUFFIX START:$START END:$END

if [[ -z "$ALGORITHM" || -z "$PREFIX" || -z "$SUFFIX" || -z "$START" || -z "$END" ]]
then
    echo usage: RL.sh [ALGORITHM] [PREFIX] [SUFFIX] [START] [END] [COMMANDPATH]
fi

until [ $START -gt $END ]; do
    echo $PREFIX/$START/$SUFFIX/shell.output:
    tail -n 2 $PREFIX/$START/$SUFFIX/shell.output
>>>>>>> origin/master
    sleep 0.5
    let START+=1
done