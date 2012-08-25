#!/usr/bin/env python2
import numpy as np

def meanMultiDim(L):
    if isinstance(L[0], list):
        rows = len(L[0])
    else:
        rows = 1
        
    if isinstance(L[0][0], list):
        cols = len(L[0][0])
    else:
        cols = 1

    mRow = []
    mList = []
    for row in range(rows):
        mRow = []
        for col in range(cols):
            data = [l[row][col] for l in L]
            m = np.mean(data)
            mRow.append(m)
        mList.append(mRow)
    return mList

def confidenceIntervalMultiDim(L, m = None):
    if m == None:
        # calculate the mean values using meanMultiDim
        m = meanMultiDim(L)
        
    # calculate the error
    rows = len(L[0])
    cols = len(L[0][0])

    cfdIntList = []
    for row in range(rows):
        cfdIntRow = []
        for col in range(cols):
            data = [l[row][col] for l in L]
            n = float(len(data))
            
            stdDev = np.std(data)
            stdErr = stdDev / np.sqrt(n)
            cfdInt = 1.96 * stdErr
            
            cfdIntRow.append(cfdInt)
        cfdIntList.append(cfdIntRow)
    return cfdIntList
