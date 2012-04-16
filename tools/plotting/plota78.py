#!/usr/bin/env python
import pylab as pl
import matplotlib.font_manager

def plot():
    experimento = '/home/rafaelbeirigo/ql/experiments/'
    
    prob     = pl.loadtxt(experimento + "/78/PRQL/prob/w.out")
    probDet  = pl.loadtxt(experimento + "/78/PRQL/prob.det/w.out")
    det      = pl.loadtxt(experimento + "/78/PRQL/det/w.out")

    ql = pl.loadtxt(experimento +   "/78/QL/w.out")

    pl.xlabel("Episodes")
    pl.ylabel("W")

    pl.plot(prob,     '-', label = r'PRQL_prob')
    pl.plot(probDet,  '-', label = r'PRQL_prob_det')
    pl.plot(det,      '-', label = r'PRQL_det')
    pl.plot(ql,       '-', label = 'Q-Learning')

    leg_prop = matplotlib.font_manager.FontProperties(size = 8)
    pl.legend(loc = 4, prop=leg_prop)
