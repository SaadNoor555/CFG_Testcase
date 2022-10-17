from os import system
import random
from CFG import *

filename = 'sld.c'
dir = '../C_Files/'
# outputName = random.randint(0,  100000)
genCFGCommand = 'gcc -fdump-tree-cfg-lineno ' + dir+filename + ' -o '+dir+filename[0]

system(genCFGCommand)

outputFileName = dir+filename[0]+'-'+filename+'.015t.cfg'
outputFile = open(outputFileName, 'r')

lines = outputFile.readlines()

nodes = [[], [2]]
e = 0
for line in lines:
    if 'succs' in line:
        tmp = []
        words = line.split(' ')
        for word in words:
            if word.isnumeric():
                tmp.append(int(word))
        nodes.append(tmp[1:])
        e+=len(tmp[1:])
    if '<bb' in 

print('Cyclometic Complexity:', e-len(nodes)+1+2)

g = Graph(len(nodes))
for i in range(1, len(nodes)):
    for node in nodes[i]:
        g.addEdge(i, node)

s, d = 1, len(nodes)-1
print ("Following are all different paths from % d to % d :" %(s, d))
g.printAllPaths(s, d)
