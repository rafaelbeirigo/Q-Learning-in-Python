#!/bin/bash

PREFIX=$1
SUFFIX=$2
START=$3
END=$4

echo PREFIX:$PREFIX SUFFIX:$SUFFIX START:$START END:$END

if [[ -z "$PREFIX" || -z "$SUFFIX" || -z "$START" || -z "$END" ]]
then
    echo usage: descompactaW_avg.sh [PREFIX] [SUFFIX] [START] [END]
fi

until [ $START -gt $END ]; do
    find $PREFIX/$START/$SUFFIX/ \
            -name 'W_avg_list_mean.out.gz'   -exec gzip -d '{}' \; -print \
        -or -name "W_avg_list_cfdInt.out.gz" -exec gzip -d '{}' \; -print
    
    let START+=1
done
