#!/bin/bash

import pylab as pl
import time

pasta = 173
for experiment in range(1, 7):
#    pl.plot(pl.loadtxt('/home/rafaelbeirigo/Dropbox/experiments/' + str(pasta) + '/' + str(experiment) + '/QL/w.out'),                      label='Q-Learning - ' + str(pasta) + ' - ' + str(experiment))
    pl.plot(pl.loadtxt('/home/rafaelbeirigo/Dropbox/experiments/' + str(pasta) + '/' + str(experiment) + '/ipmu/PRQL/W_avg_list_mean.out'), label='IPMU - ' + str(pasta) + ' - ' + str(experiment))
#    pl.plot(pl.loadtxt('/home/rafaelbeirigo/Dropbox/experiments/' + str(pasta) + '/' + str(experiment) + '/manu/PRQL/W_avg_list_mean.out'), label='Manu - ' + str(pasta) + ' - ' + str(experiment))

pasta = 175
for experiment in range(1, 2):
#    pl.plot(pl.loadtxt('/home/rafaelbeirigo/Dropbox/experiments/' + str(pasta) + '/' + str(experiment) + '/QL/w.out'),                      label='Q-Learning - ' + str(pasta) + ' - ' + str(experiment))
    pl.plot(pl.loadtxt('/home/rafaelbeirigo/Dropbox/experiments/' + str(pasta) + '/' + str(experiment) + '/ipmu/PRQL/W_avg_list_mean.out'), label='IPMU - ' + str(pasta) + ' - ' + str(experiment))
#    pl.plot(pl.loadtxt('/home/rafaelbeirigo/Dropbox/experiments/' + str(pasta) + '/' + str(experiment) + '/manu/PRQL/W_avg_list_mean.out'), label='Manu - ' + str(pasta) + ' - ' + str(experiment))

pasta = 176
for experiment in range(1, 2):
#    pl.plot(pl.loadtxt('/home/rafaelbeirigo/Dropbox/experiments/' + str(pasta) + '/' + str(experiment) + '/QL/w.out'),                      label='Q-Learning - ' + str(pasta) + ' - ' + str(experiment))
    pl.plot(pl.loadtxt('/home/rafaelbeirigo/Dropbox/experiments/' + str(pasta) + '/' + str(experiment) + '/ipmu/PRQL/W_avg_list_mean.out'), label='IPMU - ' + str(pasta) + ' - ' + str(experiment))
#    pl.plot(pl.loadtxt('/home/rafaelbeirigo/Dropbox/experiments/' + str(pasta) + '/' + str(experiment) + '/manu/PRQL/W_avg_list_mean.out'), label='Manu - ' + str(pasta) + ' - ' + str(experiment))
pl.title('')
pl.legend(loc='lower right')
