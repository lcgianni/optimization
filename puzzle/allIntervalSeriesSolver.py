#!/usr/bin/python
# -*- coding: utf-8 -*-

from constraint import *
from numpy import *

def solveIt(n):    
    problem = Problem()
    problem.addVariables(range(0, n), range(0, n))
    problem.addConstraint(AllDifferentConstraint(), range(0, n))
    
    problem.addVariables(range(n, 2*n - 1), range(1, n))
    for i in range(n - 1):
        problem.addConstraint(lambda x,y,z: abs(x-y) == z, [i, i+1, i+n]) 
    
    problem.addConstraint(AllDifferentConstraint(), range(n, 2*n - 1))
    solution = problem.getSolution()

    sol = []
    for i in range(n):
        sol.append(solution[i])
    
    # prepare the solution in the specified output format
    # if no solution is found, put 0s
    outputData = str(n) + '\n'
    if sol == None:
        print 'no solution found.'
        outputData += ' '.join(map(str, [0]*n))+'\n'
    else: 
        outputData += ' '.join(map(str, sol))+'\n'
    
    return outputData

import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            n = int(sys.argv[1].strip())
        except:
            print sys.argv[1].strip(), 'is not an integer'
        print 'Solving Size:', n
        print(solveIt(n))

    else:
        print('This test requires an instance size.  Please select the size of problem to solve. (i.e. python allIntervalSeriesSolver.py 15)')

