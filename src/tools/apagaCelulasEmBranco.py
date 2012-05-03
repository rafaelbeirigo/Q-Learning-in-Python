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

def main():
    desktop = OOoLib.getDesktop()
    doc = desktop.getCurrentComponent()
    sheet = doc.getSheets().getByIndex(0)

    col = row = 0
    cell = sheet.getCellByPosition(col, row)
    text = cell.getFormula()

    while text != 'Z':
        while text != 'Z':
            srcCoord = CellCoordinates(col, row)

            # if it is a wall-cell, jump it
            if isWall(sheet, srcCoord):
                col += 1
                text = sheet.getCellByPosition(col, row).getFormula()
                continue
            
            srcCell = sheet.getCellByPosition(srcCoord.col, \
                                              srcCoord.row)

            print srcCell.CellBackColor
            
            if srcCell.CellBackColor == 32768:
                srcState = nameState(srcCoord.col, srcCoord.row)

            col += 1
            text = sheet.getCellByPosition(col, row).getFormula()
        col = 0
        row += 1
        text = sheet.getCellByPosition(col, row).getFormula()
main()
