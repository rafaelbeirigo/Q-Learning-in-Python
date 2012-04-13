#!/usr/bin/env python
import pylab as pl

def plota37a41():
    experimento = '/home/rafaelbeirigo/ql/experiments/'
    
    prql000 = pl.loadtxt(experimento + "/37/PRQL/w.out")
    prql025 = pl.loadtxt(experimento + "/38/PRQL/w.out")
    prql050 = pl.loadtxt(experimento + "/39/PRQL/w.out")
    prql075 = pl.loadtxt(experimento + "/40/PRQL/w.out")
    prql100 = pl.loadtxt(experimento + "/41/PRQL/w.out")
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
