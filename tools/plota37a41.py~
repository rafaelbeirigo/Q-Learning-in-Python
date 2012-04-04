#!/usr/bin/env python
import pylab as pl

def plota32a36():
    experimento = '/home/rafaelbeirigo/ql/experiments/'
    
    prql000 = pl.loadtxt(experimento + "/36/PRQL/w.out")
    prql025 = pl.loadtxt(experimento + "/35/PRQL/w.out")
    prql050 = pl.loadtxt(experimento + "/34/PRQL/w.out")
    prql075 = pl.loadtxt(experimento + "/33/PRQL/w.out")
    prql100 = pl.loadtxt(experimento + "/32/PRQL/w.out")
    ql = pl.loadtxt(experimento + "/37/QL/w.out")

    pl.xlabel("Episodes")
    pl.ylabel("W")

    pl.plot(prql100,  'o', label = 'PRQ-Learning - 100% de pi-reuse')
    pl.plot(prql075,  '+', label = 'PRQ-Learning -  75% de pi-reuse')
    pl.plot(prql050, '--', label = 'PRQ-Learning -  50% de pi-reuse')
    pl.plot(prql025, '-.', label = 'PRQ-Learning -  25% de pi-reuse')
    pl.plot(prql000,  ':', label = 'PRQ-Learning -   0% de pi-reuse')

    pl.plot(ql, label = 'Q-Learning')

    pl.legend(loc = 0)
