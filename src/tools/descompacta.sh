#!/bin/bash

PREFIX=$1
SUFFIX=$2
START=$3
END=$4
FILE=$5

echo PREFIX:$PREFIX SUFFIX:$SUFFIX START:$START END:$END FILE:$FILE

if [[ -z "$PREFIX" || -z "$SUFFIX" || -z "$START" || -z "$END" || -z "$FILE" ]]
then
    echo usage: descompacta.sh [PREFIX] [SUFFIX] [START] [END] [FILE]
fi

until [ $START -gt $END ]; do
    find $PREFIX/$START/$SUFFIX/ -name "$FILE" -exec gzip -d '{}' \; -print
    let START+=1
done
