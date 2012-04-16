#!/usr/bin/env python
import pylab as pl
import matplotlib.font_manager

def plot():
    experimento = '/home/rafaelbeirigo/ql/experiments/'

    pl.title('112 a 122')
    
    pi0  = pl.loadtxt(experimento + "/112/PRQL/w.out")
    pi1  = pl.loadtxt(experimento + "/113/PRQL/w.out")
    pi2  = pl.loadtxt(experimento + "/114/PRQL/w.out")
    pi3  = pl.loadtxt(experimento + "/115/PRQL/w.out")
    pi4  = pl.loadtxt(experimento + "/116/PRQL/w.out")
    pi5  = pl.loadtxt(experimento + "/117/PRQL/w.out")
    pi6  = pl.loadtxt(experimento + "/118/PRQL/w.out")
    pi7  = pl.loadtxt(experimento + "/119/PRQL/w.out")
    pi8  = pl.loadtxt(experimento + "/120/PRQL/w.out")
    pi9  = pl.loadtxt(experimento + "/121/PRQL/w.out")
    pi10 = pl.loadtxt(experimento + "/122/PRQL/w.out")

    ql = pl.loadtxt(experimento +   "/112/QL/w.out")

    pl.xlabel("Episodes")
    pl.ylabel("W")

    intervalo  = 15
    incremento = 50

    intervalo_pi10 = intervalo; intervalo += incremento
    intervalo_pi9  = intervalo; intervalo += incremento
    intervalo_pi8  = intervalo; intervalo += incremento
    intervalo_pi7  = intervalo; intervalo += incremento
    intervalo_pi6  = intervalo; intervalo += incremento
    intervalo_pi5  = intervalo; intervalo += incremento
    intervalo_pi4  = intervalo; intervalo += incremento
    intervalo_pi3  = intervalo; intervalo += incremento
    intervalo_pi2  = intervalo; intervalo += incremento
    intervalo_pi1  = intervalo; intervalo += incremento
    intervalo_pi0  = intervalo_pi10
    intervalo_ql   = intervalo_pi10

    x_pi10    = pl.mgrid[ : pi10.shape[0] : intervalo_pi10]
    x_pi9     = pl.mgrid[ : pi7.shape[0]  : intervalo_pi9]
    x_pi8     = pl.mgrid[ : pi7.shape[0]  : intervalo_pi8]
    x_pi7     = pl.mgrid[ : pi7.shape[0]  : intervalo_pi7]
    x_pi6     = pl.mgrid[ : pi7.shape[0]  : intervalo_pi6]
    x_pi5     = pl.mgrid[ : pi7.shape[0]  : intervalo_pi5]
    x_pi4     = pl.mgrid[ : pi7.shape[0]  : intervalo_pi4]
    x_pi3     = pl.mgrid[ : pi7.shape[0]  : intervalo_pi3]
    x_pi2     = pl.mgrid[ : pi7.shape[0]  : intervalo_pi2]
    x_pi1     = pl.mgrid[ : pi7.shape[0]  : intervalo_pi1]
    x_pi0     = pl.mgrid[ : pi0.shape[0]  : intervalo_pi0]
    x_ql      = pl.mgrid[ : ql.shape[0]   : intervalo_ql]
   
    pl.plot(x_ql,     ql[::intervalo_ql],          'o', label='Q-Learning')
    pl.plot(x_pi10, pi10[::intervalo_pi10],        '*')
    pl.plot(x_pi9,   pi9[::intervalo_pi9],         '*')
    pl.plot(x_pi8,   pi8[::intervalo_pi8],         '*')
    pl.plot(x_pi7,   pi7[::intervalo_pi7],         '*')
    pl.plot(x_pi6,   pi6[::intervalo_pi6],         '*')
    pl.plot(x_pi5,   pi5[::intervalo_pi5],         '*')
    pl.plot(x_pi4,   pi4[::intervalo_pi4],         '*')
    pl.plot(x_pi3,   pi3[::intervalo_pi3],         '*')
    pl.plot(x_pi2,   pi2[::intervalo_pi2],         '*')
    pl.plot(x_pi1,   pi1[::intervalo_pi1],         '*')

    # plota linhas ate o final (com esses intervalos as vezes falta ponto no final)
    pl.plot(pi10,                          linestyle='-' , label='Otima: 100% Pessima:   0%', color='g')
    pl.plot(pi9,                           linestyle='-' , label='Otima:  90% Pessima:  10%')
    pl.plot(pi8,                           linestyle='-' , label='Otima:  80% Pessima:  20%')
    pl.plot(pi7,                           linestyle='-' , label='Otima:  70% Pessima:  30%')
    pl.plot(pi6,                           linestyle='-' , label='Otima:  60% Pessima:  40%')
    pl.plot(pi5,                           linestyle='-' , label='Otima:  50% Pessima:  50%')
    pl.plot(pi4,                           linestyle='-' , label='Otima:  40% Pessima:  60%')
    pl.plot(pi3,                           linestyle='-' , label='Otima:  30% Pessima:  70%')
    pl.plot(pi2,                           linestyle='-' , label='Otima:  20% Pessima:  80%')
    pl.plot(pi1,                           linestyle='-' , label='Otima:  10% Pessima:  90%')
    pl.plot(pi0,                           linestyle='-' , label='Otima:   0% Pessima: 100%', color='r')

    leg_prop=matplotlib.font_manager.FontProperties(size=12)
    pl.legend(loc=4, prop=leg_prop)
