import pylab as pl
import pygraphviz as pgv

def transitionsProb2graph(transitionsFile):
    T = pl.loadtxt(transitionsFile)
    
    A = pgv.AGraph(directed = True)

    for t in T:
        s1 = t[0]
        a  = t[1]
        s2 = t[2]
        p  = t[3]
        if p > 0.0:
            #A.add_edge(s1, s2, label = 'a: ' + str(a) + 'p: ' + str(p))
            A.add_edge(int(s1), int(s2))

    #print A.string() # print to screen

    A.write('simple.dot') # write to simple.dot
    print "Wrote simple.dot"

    B = pgv.AGraph('simple.dot') # create a new graph from file
    B.layout() # layout with default (neato)

    #B.draw('simple.png') # draw png
    #print "Wrote simple.png"
