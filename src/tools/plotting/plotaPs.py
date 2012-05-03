#!/usr/bin/env python
import pylab as pl
import matplotlib.font_manager
import plotErrorBar as peb
import os

def plot():
    markers = ['o', 'v', '^', '<', '>', '1', '2', '3', '4', 's', 'p', '*', 'h', 'H', '+', 'x', 'D', 'd', '|', '_']
    marker = 0
    for experiment in range(1, 37):
        directory = '/home/rafaelbeirigo/ql/experiments/167/' + str(experiment) + '/PRQL/'

        Ps        = pl.loadtxt(directory + '/Ps_mean.out')
        #prCfdInt  = pl.loadtxt(experimento + '/PRQL/W_avg_list_cfdInt.out')

        pl.xlabel("Episodes")
        pl.ylabel(r'P[\Pi]')

        policies = os.listdir(directory + '/policies/')
        policies.sort()

        # plota a primeira coluna (\Pi_\Omega)
        pi = [line[0] for line in Ps]
        pl.plot(pi, label=r'$\Pi_{\Omega}$') #, marker=markers[marker])

        col = 1
        for policy in policies:
            pi = [line[col] for line in Ps]
            #policy = int(str.split(fileName, '-')[1])
            pl.plot(pi, label=policies[col - 1]) #, marker=markers[marker])
            col += 1

        leg_prop=matplotlib.font_manager.FontProperties(size=12)
        pl.legend(loc=4, prop=leg_prop)
        pl.title(str(experiment))
        pl.savefig(directory + '/Ps.png', dpi=300)
        pl.close()

        marker += 1
