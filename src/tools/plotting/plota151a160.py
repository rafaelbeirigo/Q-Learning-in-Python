#!/usr/bin/env python
import pylab as pl
import matplotlib.font_manager
import plotErrorBar as peb
import os

def plot():
<<<<<<< HEAD
    markers = ['o', 'v', '^', '<', '>', '1', '2', '3', '4', 's', 'p', '*', 'h', 'H', '+', 'x', 'D', 'd', '|', '_']
    marker = 0
=======
>>>>>>> origin/master
    for experiment in range(151, 161):
        directory = '/home/rafaelbeirigo/ql/experiments/' + str(experiment) + '/PRQL/'

        prMean    = pl.loadtxt(directory + '/W_avg_list_mean.out')
        #prCfdInt  = pl.loadtxt(experimento + '/PRQL/W_avg_list_cfdInt.out')

        pl.xlabel("Episodes")
        pl.ylabel("W")

        policies = os.listdir(directory + '/policies/')
        print 'policies', policies

<<<<<<< HEAD
        pl.plot(prMean, label=policies[0], marker=markers[marker])
        #peb.plotErrorBar(prMean, prCfdInt)

        pl.title('')
        marker += 1

    leg_prop=matplotlib.font_manager.FontProperties(size=12)

    ## # plota o que usa todas
    ## prMean    = pl.loadtxt('/home/rafaelbeirigo/ql/experiments/161/PRQL/W_avg_list_mean.out')
    ## #prCfdInt  = pl.loadtxt('/home/rafaelbeirigo/ql/experiments/161/PRQL/W_avg_list_cfdInt.out')
    ## pl.plot(prMean, label='Todas', marker='^')
=======
        pl.plot(prMean, label=policies[0])
        #peb.plotErrorBar(prMean, prCfdInt)

        pl.title('')

    leg_prop=matplotlib.font_manager.FontProperties(size=12)

    # plota o que usa todas
    prMean    = pl.loadtxt('/home/rafaelbeirigo/ql/experiments/161/PRQL/W_avg_list_mean.out')
    #prCfdInt  = pl.loadtxt('/home/rafaelbeirigo/ql/experiments/161/PRQL/W_avg_list_cfdInt.out')
    pl.plot(prMean, label='Todas', marker='^')
>>>>>>> origin/master

    ql = pl.loadtxt('/home/rafaelbeirigo/ql/experiments/151/QL/w.out')
    pl.plot(ql, label='Q-Learning')

    pl.legend(loc=4, prop=leg_prop)
