#!/usr/bin/env python
import pylab as pl

def plot():
    experimento = '/home/rafaelbeirigo/ql/experiments/167/'

    pl.title('134 a 138')
    
    aBs = pl.loadtxt(experimento + 'W_avg_list_mean.absprob.out')
    pi  = pl.loadtxt(experimento + 'W_avg_list_mean.pi.out')
    piC = pl.loadtxt(experimento + 'W_avg_list_mean.piConc.out')

    ql = pl.loadtxt(experimento + "/1/QL/w.out")

    pl.xlabel("Episodes")
    pl.ylabel("W")

    pl.plot(aBs,  '-', label = 'absprob')
    pl.plot(pi,   '-', label = 'manu1')
    pl.plot(piC,  '-', label = 'manu2')

    pl.plot(ql, label = 'Q-Learning')

    pl.legend(loc = 0)

def main():
    plot()

    #if __name__ == "__main__":
main()
