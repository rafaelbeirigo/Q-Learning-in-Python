#!/usr/bin/env python
import pylab as pl

def plot(experimento = None):
    path = '/home/rafaelbeirigo/ql/experiments/'
    
    ql     = pl.loadtxt(path + experimento + "/w.QL.out")
    prql_p = pl.loadtxt(path + experimento + "/w.PRQL.prob.out")
    prql_d = pl.loadtxt(path + experimento + "/w.PRQL.det.out")

    pl.xlabel("Episodes")
    pl.ylabel("W")

    pl.plot(ql,     label = 'Q-Learning')
    pl.plot(prql_p, label = 'PRQ-Learning prob')
    pl.plot(prql_d, label = 'PRQ-Learning det')

    pl.legend(loc = 0)
