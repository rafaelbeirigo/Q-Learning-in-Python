#!/usr/bin/env python
import pylab as pl
import matplotlib.font_manager
import plotErrorBar as peb
import os

def plot():
    for experiment in range(151, 161):
        directory = '/home/rafaelbeirigo/ql/experiments/' + str(experiment) + '/PRQL/'

        prMean    = pl.loadtxt(directory + '/W_avg_list_mean.out')
        #prCfdInt  = pl.loadtxt(experimento + '/PRQL/W_avg_list_cfdInt.out')

        pl.xlabel("Episodes")
        pl.ylabel("W")

        policies = os.listdir(directory + '/policies/')
        print 'policies', policies

        pl.plot(prMean, label=policies[0])
        #peb.plotErrorBar(prMean, prCfdInt)

        pl.title('')

    leg_prop=matplotlib.font_manager.FontProperties(size=12)

    # plota o que usa todas
    prMean    = pl.loadtxt('/home/rafaelbeirigo/ql/experiments/161/PRQL/W_avg_list_mean.out')
    #prCfdInt  = pl.loadtxt('/home/rafaelbeirigo/ql/experiments/161/PRQL/W_avg_list_cfdInt.out')
    pl.plot(prMean, label='Todas', marker='^')

    ql = pl.loadtxt('/home/rafaelbeirigo/ql/experiments/151/QL/w.out')
    pl.plot(ql, label='Q-Learning')

    pl.legend(loc=4, prop=leg_prop)
