#!/bin/bash

$MYDIR="."

DIRS=`ls -l $MYDIR | egrep '^d' | awk '{print $8}'`

# "ls -l $MYDIR"      = get a directory listing
# "| egrep '^d'"           = pipe to egrep and select only the directories
# "awk '{print $8}'" = pipe the result from egrep to awk and print only the 8th field

# and now loop through the directories:
for DIR in $DIRS
do
echo  ${DIR}
cd ${DIR}/PRQL/policies
pwd

# junta politicas
rm policy.prob.out
cat policy.pessimal.out >> policy.prob.out
cat policy.optimal.out  >> policy.prob.out

rm policy.out
rm policy.optimal*
rm policy.pessimal*

cd ../../../
done