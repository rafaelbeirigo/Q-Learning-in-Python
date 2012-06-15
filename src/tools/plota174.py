#!/bin/bash

import pylab as pl
import time

experiment = '174'

for number in range(1, 14):
    pl.plot(pl.loadtxt('/home/rafaelbeirigo/ql/experiments/' + experiment + '/' + str(number) + '/QL/w.out'), label='Q-Learning')
    pl.plot(pl.loadtxt('/home/rafaelbeirigo/ql/experiments/' + experiment + '/' + str(number) + '/ipmu/W_avg_list_mean.out'), label='IPMU')
    pl.plot(pl.loadtxt('/home/rafaelbeirigo/ql/experiments/' + experiment + '/' + str(number) + '/manu/W_avg_list_mean.out'), label='Manu')
    pl.title('2 Mapas - ' + str(number))
    pl.legend()
    
    resp = raw_input()
    pl.clf()
