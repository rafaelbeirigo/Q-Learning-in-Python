#!/usr/bin/env python

import pylab as pl

def plotaOBixin(experimento = None):
    ql = pl.loadtxt("/home/rafaelbeirigo/ql/experiments/" + experimento + "/QL/w.out")
    prql = pl.loadtxt("/home/rafaelbeirigo/ql/experiments/" + experimento + "/PRQL/w.out")
    pl.xlabel("Episodes")
    pl.ylabel("W")
    pl.plot(ql, label = 'Q-Learning')
    pl.plot(prql, label = 'PRQ-Learning')
    pl.legend(loc = 0)
