def main():
    #abre arquivo de grafo
    #para cada aresta s1-s2 aih presente cria uma linha
    #  goto_s1_s2
    #no arquivo de actions
    f = open('/home/rafaelbeirigo/Dropbox/IC-Rafael/QLearning/python/problems/WTA/19/mapa.txt', 'r')
    g = open('/home/rafaelbeirigo/Dropbox/IC-Rafael/QLearning/python/problems/WTA/19/actions.in', 'w')

    for line in f:
        s1, s2 = line.rstrip('\n').split(' ')
        g.write('goto_' + str(s1) + '_' + str(s2) + '\n')

    f.close()
    g.close()

main()
