from os import system
import random
from CFG import *

filename = 'test.cpp'
dir = '../C++Files/'
# outputName = random.randint(0,  100000)
genCFGCommand = 'g++ -fdump-tree-cfg-lineno ' + dir+filename
print(genCFGCommand)

system(genCFGCommand)

outputFileName = filename+'.011t.cfg'
outputFile = open(outputFileName, 'r')

lines = outputFile.readlines()

nodes = [[], [2]]
code_lines = [{}, {}]
bbn = 2
fnbb = False
ll = set()
print(len(lines))
for line in lines:
    if 'succs' in line:
        tmp = []
        words = line.split(' ')
        for word in words:
            if word.isnumeric():
                tmp.append(int(word))
        nodes.append(tmp[1:])
    if '<bb '+str(bbn)+'>:' in line:
        bbn += 1
        fnbb = True
    elif fnbb == True:
        print('yooo')
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
print('lines:')
print(code_lines)
print('nodes:')
print(nodes)
for s in code_lines:
    lns = []
    for num in s:
        lns.append(num)
    vertice_list.append(Node(lns))

vertice_list.append(Node([]))
cnt = 1
print('\n****Vertices****')
for v in vertice_list[1:]:
    print('Vertice',cnt, ':', v.lines)
    cnt+=1

print('\n***GRAPH***')
edges = 0
cnt=1
# print(len(vertice_list))
for n in nodes[1:]:
    if cnt==len(vertice_list[1:]):
        print(cnt, ':', [])
        break
    edges += len(n)
    print(cnt, ':', n)
    cnt+=1
    

g = Graph(len(nodes))
for i in range(1, len(nodes)):
    for node in nodes[i]:
        g.addEdge(i, node)

print('edges:', edges)
print('nodes:', len(vertice_list[1:]))
print('\nCyclometic Complexity:', edges-len(vertice_list[1:])+2)

# s, d = 1, len(nodes)-1
# print ("Following are all different paths from % d to % d :" %(s, d))
# g.printAllPaths(s, d)
