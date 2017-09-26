#!/usr/bin/python
# -*- coding: utf-8 -*-

from coinor.pulp import *  # Import the module

pulp.pulpTestAll()

def solveIt(inputData):
    # parse the input
    lines = inputData.split('\n')

    firstLine = lines[0].split()
    items = int(firstLine[0])
    capacity = int(firstLine[1])
    
    values = []
    weights = []

    for i in range(1, items+1):
        line = lines[i]
        parts = line.split()

        values.append(int(parts[0]))
        weights.append(int(parts[1]))
        

    items = range(items)
    prob = LpProblem("Warehouse", LpMaximize)
    
    # x variable = uses warehouse i or not
    x = LpVariable.dicts("TakeItem", items, 0, 1, LpBinary)
    
    prob += lpSum(values[i]*x[i] for i in items)
    prob += lpSum(weights[i]*x[i] for i in items) <= capacity-500
        
    prob.solve()
    
    value = 0
    for i in items:
       if x[i].varValue == 1:
           value += values[i]
           
    taken = []
    
    for i in items:
        taken.append(int(x[i].varValue))

    # prepare the solution in the specified output format
    outputData = str(value) + ' ' + str(0) + '\n'
    outputData += ' '.join(map(str, taken))
    
    return outputData


import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        fileLocation = sys.argv[1].strip()
        inputDataFile = open(fileLocation, 'r')
        inputData = ''.join(inputDataFile.readlines())
        inputDataFile.close()
        print solveIt(inputData)
    else:
        print 'This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)'

