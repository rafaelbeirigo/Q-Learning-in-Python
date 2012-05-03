#coding: utf-8 
import pylab as pl

def main():
    psi = 1.0
    v = 1.0


    for d in range(1):
        P_PI_past = []
        P_PI_new = []; P_PI_new_bottom = []
        P_PI_r = []

        psi = 1.0
        v = 0.95
        qtd = 100
        for i in range(qtd):
            P_PI_past.append(psi)
            
            P_PI_r.append((1 - psi) * psi)

            P_PI_new.append((1 - psi) * (1 - psi))
            P_PI_new_bottom.append(P_PI_past[i] + P_PI_r[i])

            psi = psi * v

        pl.title(u'Probabilidades de aplicação de políticas internamente ao ' + \
                 r'$\pi$-reuse' + r', ($\psi$=1.0, $v$=0.95, 100 passos)')

        pl.bar(range(qtd), P_PI_past,                           color='blue',  label=u'P($\Pi_{past}$)', linewidth=None)
        pl.bar(range(qtd), P_PI_r,      bottom=P_PI_past,       color='red',   label=u'P($\Pi_{r}$)',    linewidth=None)
        pl.bar(range(qtd), P_PI_new,    bottom=P_PI_new_bottom, color='green', label=u'P($\Pi_{new}$)',  linewidth=None)

        pl.show()
        pl.legend(loc='bottom')
main()
