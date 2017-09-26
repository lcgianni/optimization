#!/usr/bin/python
# -*- coding: utf-8 -*-

from coinor.pulp import *  # Import the module

def solveIt(inputData):
    # parse the input
    lines = inputData.split('\n')

    parts = lines[0].split()
    warehouseCount = int(parts[0])
    customerCount = int(parts[1])

    warehouses = []
    for i in range(1, warehouseCount+1):
        line = lines[i]
        parts = line.split()
        warehouses.append((int(parts[0]), float(parts[1])))

    customerSizes = []
    customerCosts = []

    lineIndex = warehouseCount+1
    for i in range(0, customerCount):
        customerSize = int(lines[lineIndex+2*i])
        customerCost = map(float, lines[lineIndex+2*i+1].split())
        customerSizes.append(customerSize)
        customerCosts.append(customerCost)
    
    numberWarehouses = range(len(warehouses))
    
    capacityWarehouses = []
    for i in numberWarehouses:
        info = warehouses[i]
        capacityWarehouses.append(info[0])
        
    costWarehouses = []
    for i in numberWarehouses:
        info = warehouses[i]
        costWarehouses.append(info[1])
    
    numberCustomers = range(len(customerSizes))

    # minimization problem
    prob = LpProblem("Warehouse",LpMinimize)

    # x variable = uses warehouse i or not
    x = LpVariable.dicts("UseWarehouse", numberWarehouses, 0, 1, LpBinary)
    
    # y variable = assigns warehouse i to customer j
    y = LpVariable.dicts("AssignWarehouse",[(i,j) for i in numberWarehouses for j in numberCustomers],0,1,LpBinary)
    
    # objective function
    prob += lpSum([x[i]*costWarehouses[i] for i in numberWarehouses]+[y[(i,j)]*customerCosts[j][i] for i in numberWarehouses for j in numberCustomers])
        
    # constraint 1
    for i in numberWarehouses:
        prob += lpSum(y[(i,j)]*customerSizes[j] for j in numberCustomers) <= capacityWarehouses[i]*x[i]
        
    # constraint 2
    for j in numberCustomers:
        prob += lpSum(y[(i,j)] for i in numberWarehouses) == 1
    
    # solves problem        
    prob.solve()

    # prints objective value
    obj = 0
    for i in numberWarehouses:
        obj += costWarehouses[i]*x[i].varValue
    
	solution = []
    for j in numberCustomers:
        for i in numberWarehouses:
            if y[(i,j)].varValue == 1: 
                info = customerCosts[j]
                obj += info[i]
				solution.append(i)

    # prepare the solution in the specified output format
    outputData = str(obj) + ' ' + str(0) + '\n'
    outputData += ' '.join(map(str, solution))

    return outputData


import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        fileLocation = sys.argv[1].strip()
        inputDataFile = open(fileLocation, 'r')
        inputData = ''.join(inputDataFile.readlines())
        inputDataFile.close()
        print 'Solving:', fileLocation
        print solveIt(inputData)
    else:
        print 'This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/wl_16_1)'

