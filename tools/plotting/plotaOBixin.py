#!/usr/bin/env python
import pylab as pl

def plot(experimento = None):
    path = '/home/rafaelbeirigo/ql/experiments/'
    
    ql = pl.loadtxt(path + experimento + "/QL/w.out")
    prql = pl.loadtxt(path + experimento + "/PRQL/w.out")

    pl.xlabel("Episodes")
    pl.ylabel("W")

    pl.plot(ql, label = 'Q-Learning')
    pl.plot(prql, label = 'PRQ-Learning prob')

    pl.legend(loc = 0)
