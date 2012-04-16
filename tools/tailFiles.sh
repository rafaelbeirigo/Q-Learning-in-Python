#!/bin/bash

FILENAME=$1
START=$2
END=$3

until [  $START -gt $END ]; do
    echo '/home/rafaelbeirigo/ql/experiments/tests/porcents/eGreedy/'$START'/'$FILENAME:
    tail '/home/rafaelbeirigo/ql/experiments/tests/porcents/eGreedy/'$START'/'$FILENAME
    let START+=1
done