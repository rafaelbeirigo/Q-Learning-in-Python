import os
import meanError
import pylab as pl
#import Danny.OOo.OOoLib as OOoLib
#from com.sun.star.table.CellContentType import TEXT, EMPTY, VALUE, FORMULA

# the following command must be executed in a terminal BEFORE executing
# this script:
# ooffice "-accept=socket,host=localhost,port=8100;urp;"

def meanOfMeans():
    initialExperiment = 25
    finalExperiment   = 35
    suffix            = 'piConc'
    experimentFolder  = '170'

    rootDir = os.path.join('/', 'home', 'rafaelbeirigo', 'ql', 'experiments',
                           experimentFolder)

    means = []
    meanFileName = 'W_avg_list_mean.out'
    for experiment in range(initialExperiment, finalExperiment + 1):
        meanFilePath = os.path.join(rootDir, str(experiment), 'PRQL', meanFileName)
        # open experiment the file that contains the "individual" mean
        # into a list
        mean = pl.loadtxt(meanFilePath)

        # this must be done because the function meanError.meanMultiDim()
        # needs each item in the mean list to be a list itself.
        mean = [[item] for item in mean]

        # append it to the list of means
        means.append(mean)

    # obtain the global mean considering the list of individual means
    globalMean = meanError.meanMultiDim(means)
    ## print globalMean

    #means2spreadsheet([globalMean])
    
    pl.savetxt(os.path.join(rootDir, 'W_avg_list_mean.' + suffix + '.out'),
               globalMean, fmt='%1.6f')

    return globalMean

def means2spreadsheet(means):
    desktop = OOoLib.getDesktop()
    doc = desktop.getCurrentComponent()
    sheet = doc.getSheets().getByIndex(0)

    col = 0
    for mean in means:
        row = 0
        for m in mean:
            sheet.getCellByPosition(col, row).setFormula(float(m[0]))
            row += 1
        col  += 1

def main():
    #means2spreadsheet(meanOfMeans())
    meanOfMeans()
    
main()
