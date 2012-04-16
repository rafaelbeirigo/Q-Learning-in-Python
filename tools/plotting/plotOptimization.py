#!/usr/bin/env python
import pylab as pl

def plot():
    experimento = '/home/rafaelbeirigo/ql/experiments/'

    pl.title('Optimization Test 01 - Parameters via command line')
    
    newP = pl.loadtxt(experimento + "/tests/01/PRQL/w.out")
    oldP = pl.loadtxt(experimento + "/149/PRQL/w.out")

    newQ = pl.loadtxt(experimento + "/tests/01/QL/w.out")
    oldQ = pl.loadtxt(experimento + "/139/QL/w.out")

    pl.xlabel("Episodes")
    pl.ylabel("W")

    pl.plot(oldP, '-', label='oldP')
    pl.plot(newP, '-', label='newP')
    pl.plot(oldQ, '-', label='oldQ')
    pl.plot(newQ, '-', label='newQ')

    pl.legend(loc = 0)
