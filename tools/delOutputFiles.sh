#!/bin/bash

if [ -z $1 ]; then
    echo 'Please inform the path'
else
    echo 'Deleting output files...'
    find $1 -name '*.out' -exec rm '{}' \; -print
    echo 'Deletion is done'
fi
