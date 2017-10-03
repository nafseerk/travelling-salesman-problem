from tsp_data import TSPData
from tspHelper import TSPHelper
from tspState import TSPState
from tsp_open_list import TSPOpenList
from tsp_closed_list import TSPClosedList
import pprint
import time

def AstarSearch(initialState, openList, closedList, verbose=0):
    startTime = time.time()
    if verbose == 2: print('Astar search starting with state:' + initialState.getPath())
    openList.add(initialState)
    currentState = openList.getItem()
    
    while not currentState.isGoalState():
        if verbose == 2: print('At state:' + currentState.getPath())

        #Add the current state into closedList
        closedList.add(currentState)
        
        #Generate all successors of current state and add them to openList if not already closed
        successors = currentState.getSuccessors()
        for successor in successors:
            if closedList.hasState(successor) == False:
                openList.add(successor)

        nextState = openList.getItem()
        currentState = currentState.moveToNextState(nextState)
        if verbose == 2: print('Moving to next state:%s with f=%.2f g=%.2f h=%.2f' \
                          % (nextState.getPath(), nextState.fOfState(), nextState.gOfState(), nextState.hOfState()))

        currentTime = time.time()
        #Stop the execution if it took longer than 10 mins
        if (currentTime - startTime)/60 > 10:
            return None

    if verbose >= 1:
        print('A* search complete: Solution = %s with cost = %.2f' % (currentState.getPath(), currentState.gOfState()))
        print('No of nodes expanded = %d' % openList.getExpandedStatesCount())
        print('execution completed in %f mins' % ((currentTime - startTime)/60))
    return currentState 


if __name__ == '__main__':
    #Test the A*search
    inputFilePath = '/Users/apple/Documents/Projects/randTSP/10/instance_1.txt'
    tspData = TSPData(inputFilePath)
    print('Testing A*search on the below data')
    tspData.summary()
    tspHelper = TSPHelper(tspData, noHeuristic=False)
    tspHelper.setStartCity('A')
    initialState = TSPState(tspHelper,'A')
    openList = TSPOpenList()
    closedList = TSPClosedList()
    goalState = AstarSearch(initialState, openList, closedList, verbose=1)
    if goalState == None:
        print('Took too long to find a solution....terminating')
    else:    
        print('Tour for the salesman = %s with distance = %.2f units' % (goalState.getPath(), goalState.gOfState()))
