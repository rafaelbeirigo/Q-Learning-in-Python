#!/usr/bin/env python
import MDP
import Agent
import PRQLearning
import time
import sys
import pylab as pl
from prepareFolders import prepareFolders
import getopt

def usage():
    print 'entrou na usage'

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "", ["help", "output="])
    except getopt.GetoptError, err:
        # print help information and exit:
        print str(err) # will print something like "option -a not recognized"
        usage()
        sys.exit(2)

if __name__ == "__main__":
    main()
