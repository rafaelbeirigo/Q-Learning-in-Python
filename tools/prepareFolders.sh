#!/bin/bash
MODULE='[prepareFolders.sh] :'
if [ -z $1 ]; then
    echo $MODULE + 'Please inform the path'
else
    echo $MODULE 'Deleting output files...'
    find $1 -name '*.out'    -exec rm '{}' \; -print
    find $1 -name '*.out.gz' -exec rm '{}' \; -print

    echo $MODULE 'Deleting log file...'
    find $1/../ -name 'log.txt' -exec rm '{}' \; -print
    find $1/../ -name 'log.txt.gz' -exec rm '{}' \; -print

    echo $MODULE 'Deleting graph files...'
    find $1/../ -name 'w.png' -exec rm '{}' \; -print

    echo $MODULE 'Deleting backup files...'
    find $1 -name '*~' -exec rm '{}' \; -print

    echo $MODULE 'Deletion is done'
    
    echo $MODULE 'Uncompressing input files...'
    find $1 -name '*.in.gz' -exec gzip -d '{}' \; -print
    echo $MODULE 'Uncompression is done'
fi
