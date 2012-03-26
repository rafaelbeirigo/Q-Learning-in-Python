# Read an MDP from a spreadsheet
#
# following the instructions present in:
# http://stuvel.eu/ooo-python
import Danny.OOo.OOoLib as OOoLib

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
            print row, col, sheet.getCellByPosition(col, row).getFormula()
            col += 1
            text = sheet.getCellByPosition(row, col).getFormula()
        row += 1
        col = 0
        text = sheet.getCellByPosition(row, col).getFormula()
main()
