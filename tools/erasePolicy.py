# Read an MDP from a spreadsheet
#
# following the instructions present in:
# http://stuvel.eu/ooo-python
import Danny.OOo.OOoLib as OOoLib
from com.sun.star.table.CellContentType import TEXT, EMPTY, VALUE, FORMULA

def main():
    desktop = OOoLib.getDesktop()
    doc = desktop.getCurrentComponent()

    # Insert code from above to get the document
    # reference 'doc'.

    sheet = doc.getSheets().getByIndex(0)

    row = 0
    col = 0
    text = sheet.getCellByPosition(row, col).getFormula()
    while text != 'Z':
        while text != 'Z':
            if text == u"\u2190" or \
               text == u"\u2191" or \
               text == u"\u2192" or \
               text == u"\u2193" or \
               text == 'N' or \
               text == 'S' or \
               text == 'W' or \
               text == 'E':

                sheet.getCellByPosition(col, row).setFormula('')

            col += 1
            text = sheet.getCellByPosition(col, row).getFormula()
            
        row += 1
        col = 0
        text = sheet.getCellByPosition(col, row).getFormula()

main()
