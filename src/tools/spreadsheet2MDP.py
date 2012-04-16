#!/usr/bin/env python
# Read an MDP from a spreadsheet
#
# following the instructions present in:
# http://stuvel.eu/ooo-python

import Danny.OOo.OOoLib as OOoLib
from com.sun.star.table.CellContentType import TEXT, EMPTY, VALUE, FORMULA
import sys

class CellCoordinates:
    def __init__(self, col, row):
        self.col = col
        self.row = row

class ActionAndIncrements:
    def __init__(self, action, colIncrement, rowIncrement):
        self.action = action
        self.colIncrement = colIncrement
        self.rowIncrement = rowIncrement
        
def main():
    desktop = OOoLib.getDesktop()
    doc = desktop.getCurrentComponent()
    sheet = doc.getSheets().getByIndex(0)

    col = row = 0
    cell = sheet.getCellByPosition(col, row)
    text = cell.getFormula()

    S = []
    A = resolveActions()
    T = []
    R = []
    G = []
    while text != 'Z':
        while text != 'Z':
            srcCoord = CellCoordinates(col, row)

            # if it is a wall-cell, jump it
            if isWall(sheet, srcCoord):
                col += 1
                text = sheet.getCellByPosition(col, row).getFormula()
                continue
            
            srcState = nameState(srcCoord.col, srcCoord.row)
            S.append(srcState)

            resolveGoal(sheet, srcCoord, G)

            for a in A:
                resolveTransitionAndReward(sheet, srcCoord, a, T, R, G)
            
            col += 1
            text = sheet.getCellByPosition(col, row).getFormula()
        col = 0
        row += 1
        text = sheet.getCellByPosition(col, row).getFormula()

    list2file   (S, sys.argv[1] + 'states.in')
    actions2file(A, sys.argv[1] + 'actions.in')
    list2file   (T, sys.argv[1] + 'transitions.in')
    list2file   (R, sys.argv[1] + 'rewards.in')
    list2file   (G, sys.argv[1] + 'goals.in')

def nameState(col, row):
    name = 'row' + str(row) + 'col' + str(col)
    return name

def resolveActions():
    A = []
    A.append(ActionAndIncrements('North',  0, -1))
    A.append(ActionAndIncrements('South',  0, +1))
    A.append(ActionAndIncrements('West' , -1,  0))
    A.append(ActionAndIncrements('East' , +1,  0))
    return A

def resolveTransitionAndReward(sheet, srcCoord, a, T, R, G):
    srcState = nameState(srcCoord.col, srcCoord.row)
    
    # if it is a goal state, adds only the transition to itself
    # it is not possible for the agent to receive reward acting
    # from a goal state, thus, there's no reward to resolve in
    # such a case
    if srcState in G:
        T.append(srcState + ' ' + a.action + ' ' + srcState + ' ' + str(1.0))
        return

    tgtCoord = CellCoordinates(srcCoord.col + a.colIncrement, \
                               srcCoord.row + a.rowIncrement)
    tgtCell = sheet.getCellByPosition(tgtCoord.col, \
                                      tgtCoord.row)
    if tgtCell.getType() == TEXT:
        # there's a wall: the action makes the agent
        # stay on the same state
        tgtState = srcState
    else:
        tgtState = nameState(tgtCoord.col, \
                             tgtCoord.row)

        r = tgtCell.getValue()
        if r > 0.0:
            R.append(srcState + ' ' + a.action + ' ' + str(r))

    t = srcState + ' ' + a.action + ' ' + tgtState + ' ' + str(1.0)
    T.append(t)

def resolveGoal(sheet, srcCoord, G):
    srcCell = sheet.getCellByPosition(srcCoord.col, \
                                      srcCoord.row)
    
    isGoalState = False
    if srcCell.CellBackColor == 32768:
        isGoalState = True
        srcState = nameState(srcCoord.col, srcCoord.row)
        G.append(srcState)

    return isGoalState, G

def list2file(L, file):
    f = open(file, 'w')
    for l in L:
        f.write(l + '\n')
    f.close()

def actions2file(A, file):
    f = open(file, 'w')
    for a in A:
        f.write(a.action + '\n')
    f.close()

def isWall(sheet, srcCoord):
    srcCell = sheet.getCellByPosition(srcCoord.col, \
                                      srcCoord.row)
    if srcCell.getType() == TEXT:
        text = srcCell.getFormula()
        if text == 'X':
            return True
        else:
            return False
    else:
        return False
    
main()
