def main():
    #abre arquivo de grafo
    #para cada aresta s1-s2 aih presente cria uma linha
    #  goto_s1_s2
    #no arquivo de actions
    f = open('/home/rafaelbeirigo/Dropbox/IC-Rafael/QLearning/python/problems/WTA/19/mapa.txt', 'r')
    g = open('/home/rafaelbeirigo/Dropbox/IC-Rafael/QLearning/python/problems/WTA/19/transitions.in', 'w')

    for line in f:
        s1, s2 = line.rstrip('\n').split(' ')
        g.write(str(s1) + ' ') #original state
        g.write('goto_' + str(s1) + '_' + str(s2) + ' ') #action
        g.write(str(s2) + ' 1.0\n')#final state

    f.close()
    g.close()

main()
