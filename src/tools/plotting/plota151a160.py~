#!/usr/bin/env python
import pylab as pl
import matplotlib.font_manager
import plotErrorBar as peb

def plot():
    for experimento in range(151, 160)
        experimento = '/home/rafaelbeirigo/ql/experiments/' + str(experimento) + '/'

        pl.title('')

        prMean    = pl.loadtxt(experimento + '/PRQL/W_avg_list_mean.out')
        prCfdInt  = pl.loadtxt(experimento + '/PRQL/W_avg_list_cfdInt.out')

        #ql        = pl.loadtxt(experimento + '/1/QL/w.out')

        pl.xlabel("Episodes")
        pl.ylabel("W")

        pl.plot(prMean)
        peb.plotErrorBar(prMean, prCfdInt)

        #pl.plot(ql)

    leg_prop=matplotlib.font_manager.FontProperties(size=12)
    pl.legend(loc=4, prop=leg_prop)
