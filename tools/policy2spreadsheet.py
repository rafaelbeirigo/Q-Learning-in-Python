#!/usr/bin/env python
# Read an MDP from a spreadsheet
#
# following the instructions present in:
# http://stuvel.eu/ooo-python
import sys
import itertools
import Danny.OOo.OOoLib as OOoLib
from com.sun.star.table.CellContentType import TEXT, EMPTY, VALUE, FORMULA

def main():
    desktop = OOoLib.getDesktop()
    doc = desktop.getCurrentComponent()

    # Insert code from above to get the document
    # reference 'doc'.

    sheet = doc.getSheets().getByIndex(0)

    P = []
    f = open(sys.argv[1] + 'policy.out')
    for line in f:
        row = line[:line.find('col')]
        row = row.replace('row','')
        
        col = line[line.find('col'):]
        col = col.replace('col','')

        action = line.split()[1]

        p = []
        p.append(col)
        p.append(row)
        p.append(action)
        P.append(p)

    for p in P:
        value = sheet.getCellByPosition(p[0], p[1]).getValue()
        if value:
            pass
        else:
            if p[2] == 'North': c = u"\u2191"
            if p[2] == 'South': c = u"\u2193"
            if p[2] == 'West': c = u"\u2190"
            if p[2] == 'East': c = u"\u2192"
            sheet.getCellByPosition(p[0], p[1]).setFormula(c)
    
main()
