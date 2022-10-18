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
code_lines = [{}, {}]
e = 0
bbn = 2
fnbb = False
ll = set()
for line in lines:
    if 'succs' in line:
        tmp = []
        words = line.split(' ')
        for word in words:
            if word.isnumeric():
                tmp.append(int(word))
        nodes.append(tmp[1:])
        e+=len(tmp[1:])
    if '<bb '+str(bbn)+'> :' in line:
        bbn += 1
        fnbb = True
    elif fnbb == True:
        words = line.split(':')
        if len(words)==1:
            fnbb = False
            code_lines.append(ll)
            ll = set()
        for word in  words:
            if word.isnumeric():
                ll.add(int(word))
                break

vertice_list = []

for s in code_lines:
    lns = []
    for num in s:
        lns.append(num)
    vertice_list.append(Node(lns))

cnt = 1
print('\n****Vertices****')
for v in vertice_list[1:]:
    print('Vertice',cnt, ':', v.lines)
    cnt+=1

print('\n***GRAPH***')
cnt=1
for n in nodes[1:]:
    print(cnt, ':', n)
    cnt+=1

g = Graph(len(nodes))
for i in range(1, len(nodes)):
    for node in nodes[i]:
        g.addEdge(i, node)

print('\nCyclometic Complexity:', e-len(nodes)+1+2)

s, d = 1, len(nodes)-1
print ("Following are all different paths from % d to % d :" %(s, d))
g.printAllPaths(s, d)
