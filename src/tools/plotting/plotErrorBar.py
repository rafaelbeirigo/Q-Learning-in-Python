import pylab as pl

def plotErrorBar(y, yerr, start = None, end = None, step = None):
    if start == None:
        start = 0
    if end == None:
        end   = 2000
    if step == None:
        step  = (end - start) / 20

    interval = range(start, end - 1, step)
    if interval[-1] != end - 1:
        interval.append(end - 1)

    x    = interval
    #y    = pl.loadtxt('/home/rafaelbeirigo/ql/experiments/tests/porcents/001/epsilon-greedy/149/PRQL/W_avg_list_mean.out')
    #yerr = pl.loadtxt('/home/rafaelbeirigo/ql/experiments/tests/porcents/001/epsilon-greedy/149/PRQL/W_avg_list_cfdInt.out')

    xInterval = x
    yInterval = [y[i] for i in interval]
    yerrInterval = [yerr[i] for i in interval]

    #pl.plot(y)
    pl.errorbar(xInterval, yInterval, yerrInterval, linestyle='')
