#!/usr/bin/env python
import pylab as pl
import matplotlib.font_manager
import plotErrorBar as peb
import os

def plot():
    pl.xlabel("Episodes")
    pl.ylabel("W")

    pl.title('')

    prManu = pl.loadtxt('/home/rafaelbeirigo/ql/experiments/163/PRQL/W_avg_list_mean.out')
    prIPMU = pl.loadtxt('/home/rafaelbeirigo/ql/experiments/164/PRQL/W_avg_list_mean.out')
    ql     = pl.loadtxt('/home/rafaelbeirigo/ql/experiments/163/QL/w.out')

    pl.plot(prManu, label='Manu')
    pl.plot(prIPMU, label='IPMU')
    pl.plot(ql,     label='Q-Learning')

    leg_prop=matplotlib.font_manager.FontProperties(size=12)
    pl.legend(loc=4, prop=leg_prop)
