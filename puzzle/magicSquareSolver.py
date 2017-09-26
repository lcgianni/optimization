#!/usr/bin/python
# -*- coding: utf-8 -*-

from constraint import *

def solveIt(n):
    size = n*n
    sumofsquare = sum(range(1, n*n+1))/n

    problem = Problem()

    problem.addVariables(range(0, size), range(1, size + 1))
    problem.addConstraint(AllDifferentConstraint(), range(0, size))

    diagonal1 = []
    index = - n - 1
    for i in range(n):
        index += n + 1
        diagonal1.append(index)
    
    problem.addConstraint(ExactSumConstraint(sumofsquare), diagonal1)

    diagonal2 = []
    index = 0
	for i in range(n):
        index += n - 1
        diagonal2.append(index)
    
    problem.addConstraint(ExactSumConstraint(sumofsquare), diagonal2)

    for i in range(n):
        problem.addConstraint(ExactSumConstraint(sumofsquare), [i*n + j for j in range(n)])
        
    for i in range(n):
        problem.addConstraint(ExactSumConstraint(sumofsquare), [i + n*j for j in range(n)])

    index = - n - 1
    for i in range(n-1):
        index += n + 1
        problem.addConstraint(lambda x,y: x < y, [index, index + n + 1]) 

    solution = problem.getSolution()
    
    if solution is None:
        sol is None
    else:
        sol = []
        for i in range(len(solution)):
            sol.append(solution[i])
   
    # prepare the solution in the specified output format
    # if no solution is found, put 0s
    outputData = str(n) + '\n'
    
    if sol == None:
        print 'no solution found.'
        
    else: 
        for i in range(0,n):
            outputData += ' '.join(map(str, sol[i*n:(i+1)*n]))+'\n'
    
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
        print('This test requires an instance size.  Please select the size of problem to solve. (i.e. python magicSquareSolver.py 5)')

