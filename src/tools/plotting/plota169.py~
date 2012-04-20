#!/usr/bin/env python
import pylab as pl
import os

def plot():
    experiment = '168'
    dirExp = os.path.join('/', 'home', 'rafaelbeirigo', 'ql', 'experiments', experiment)
    
    aBs = pl.loadtxt(dirExp + '/W_avg_list_mean.absprob.out')
    pi  = pl.loadtxt(dirExp + '/W_avg_list_mean.pi.out')
    piC = pl.loadtxt(dirExp + '/W_avg_list_mean.piConc.out')

    ql = pl.loadtxt(dirExp + '/1/QL/w.out')

    pl.title(experiment)
    pl.xlabel("Episodes")
    pl.ylabel("W")

    lim = 3999
    pl.plot(aBs[:lim],  '-', label = 'absprob'    + experiment)
    pl.plot(pi[:lim],   '-', label = 'manu1'      + experiment)
    pl.plot(piC[:lim],  '-', label = 'manu2'      + experiment)
    pl.plot(ql[:lim],        label = 'Q-Learning' + experiment)


    pl.legend(loc = 0)

def main():
    plot()

main()
