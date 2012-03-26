# Read an MDP from a spreadsheet
#
# following the instructions present in:
# http://stuvel.eu/ooo-python
import Danny.OOo.OOoLib as OOoLib
from com.sun.star.table.CellContentType import TEXT, EMPTY, VALUE, FORMULA
import sys

class stateCell:
    def __init__(self, col, row):
        self.col = col
        self.row = row

def main():
    desktop = OOoLib.getDesktop()
    doc = desktop.getCurrentComponent()

    # Insert code from above to get the document
    # reference 'doc'.

    sheet = doc.getSheets().getByIndex(0)

    row = 0
    col = 0
    cell = sheet.getCellByPosition(col, row)
    text = cell.getFormula()

    S = []
    T = []
    R = []
    G = []
    while text != 'Z':
        while text != 'Z':
            currentCell = sheet.getCellByPosition(col, row)

            targetCell = sheet.getCellByPosition(col, row - 1)

            resolveTransition(currentCell, targetCell)

            cellType = currentCell.getType()

            if cellType == TEXT:
                # It is a 'X'-cell, in other words, a wall
                # Nothing to do here
                pass
            else:
                # It is a normal cell
                # create the state s
                s = 'row' + str(row) + 'col' + str(col)
                S.append(s)

                # North neighbor
                if sheet.getCellByPosition(col, row - 1).getType() == TEXT:
                    pass
                else:
                    s2 = nameState(col, row - 1)

                    r0 = sheet.getCellByPosition(col, row).getValue()
                    if r0:
                        pass
                    else:
                        T.append(s + ' North ' +  s2 + ' ' + str(1.0))

                    # resolve rewards
                    r = sheet.getCellByPosition(col, row - 1).getValue()
                    if r:
                        rStr = s + ' ' + 'North' + ' ' + str(r)
                        R.append(rStr)

                # South neighbor
                if sheet.getCellByPosition(col, row + 1).getType() == TEXT:
                    pass
                else:
                    s2 = 'row' + str(row + 1) + 'col' + str(col)

                    r0 = sheet.getCellByPosition(col, row).getValue()
                    if r0:
                        pass
                    else:
                        T.append(s + ' South ' +  s2 + ' ' + str(1.0))

                    # resolve rewards
                    r = sheet.getCellByPosition(col, row + 1).getValue()
                    if r:
                        rStr = s + ' ' + 'South' + ' ' + str(r)
                        R.append(rStr)

                # West neighbor
                if sheet.getCellByPosition(col - 1, row).getType() == TEXT:
                    pass
                else:
                    s2 = 'row' + str(row) + 'col' + str(col - 1)

                    r0 = sheet.getCellByPosition(col, row).getValue()
                    if r0:
                        pass
                    else:
                        T.append(s + ' West ' +  s2 + ' ' + str(1.0))

                    # resolve rewards
                    r = sheet.getCellByPosition(col - 1, row).getValue()
                    if r != 0:
                        rStr = s + ' ' + 'West' + ' ' + str(r)
                        R.append(rStr)

                # East neighbor
                if sheet.getCellByPosition(col + 1, row).getType() == TEXT:
                    pass
                else:
                    s2 = 'row' + str(row) + 'col' + str(col + 1)

                    r0 = sheet.getCellByPosition(col, row).getValue()
                    if r0:
                        pass
                    else:
                        T.append(s + ' East ' +  s2 + ' ' + str(1.0))

                    # resolve rewards
                    r = sheet.getCellByPosition(col + 1, row).getValue()
                    if r != 0:
                        rStr = s + ' ' + 'East' + ' ' + str(r)
                        R.append(rStr)

                if currentCell.CellBackColor == 32768:
                    G.append(s)

            col += 1
            text = sheet.getCellByPosition(col, row).getFormula()
            
        row += 1
        col = 0
        text = sheet.getCellByPosition(col, row).getFormula()

    f = open(sys.argv[1] + 'states.in', 'w')
    for s in S:
        f.write(s + '\n')
    f.close()

    f = open(sys.argv[1] + 'actions.in', 'w')
    f.write('North\n')
    f.write('South\n')
    f.write('West\n')
    f.write('East\n')
    f.close()

    f = open(sys.argv[1] + 'transitions.in', 'w')
    for t in T:
        f.write(t + '\n')
    f.close()

    f = open(sys.argv[1] + 'rewards.in', 'w')
    for r in R:
        f.write(r + '\n')
    f.close()
    
    f = open(sys.argv[1] + 'goals.in', 'w')
    for g in G:
        f.write(g + '\n')
    f.close()

def nameState(col, row):
    name = 'row' + str(row) + 'col' + str(col)
    return name

def resolveTransition(currentCell, targetCell):
    if targetCell.getType() == TEXT:
        pass
    else:
        s2 = nameState(col, row - 1)

        r0 = sheet.getCellByPosition(col, row).getValue()
        if r0:
            pass
        else:
            T.append(s + ' North ' +  s2 + ' ' + str(1.0))

        # resolve rewards
        r = sheet.getCellByPosition(col, row - 1).getValue()
        if r:
            rStr = s + ' ' + 'North' + ' ' + str(r)
            R.append(rStr)

main()
