#!/usr/bin/python
# -*- coding: utf-8 -*-

from constraint import *

def solveIt(inputData):
    # parse the input
    lines = inputData.split('\n')

    firstLine = lines[0].split()
    nodeCount = int(firstLine[0])
    edgeCount = int(firstLine[1])

    edges = []
    for i in range(1, edgeCount + 1):
        line = lines[i]
        parts = line.split()
        edges.append((int(parts[0]), int(parts[1])))
    
    i = 0
    sols = None
    
    while sols is None:
        maxColors = i + 1
        model = Problem()
        model.addVariables(range(nodeCount), range(0, maxColors))
    
        for i in range(len(edges)):
            thisedge = edges[i]
            first = thisedge[0]
            second = thisedge[1]
            model.addConstraint(AllDifferentConstraint(), [first,second])
        
        sols = model.getSolution()
    
    solution = []
    for i in range(nodeCount):        
        solution.append(sols[i]-1)

    return solution


import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        fileLocation = sys.argv[1].strip()
        inputDataFile = open(fileLocation, 'r')
        inputData = ''.join(inputDataFile.readlines())
        inputDataFile.close()
        print solveIt(inputData)
    else:
        print 'This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/gc_4_1)'

