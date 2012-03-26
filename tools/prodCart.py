import sys
import itertools

f = open(sys.argv[1])
g = open(sys.argv[2])

a = []
for l in f.readlines():
    a.append(l.strip())

b = []
for l in g.readlines():
    b.append(l.strip())

for x, y, z in itertools.product(a, b, a):
    if not (x == y):
        print x, y, z, 0
