from tsp_data import TSPData
from tspHelper import TSPHelper
from tspState import TSPState
from tsp_open_list import TSPOpenList
from tsp_closed_list import TSPClosedList
import pprint

def AstarSearch(initialState, openList, closedList, verbose=0):
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

    if verbose >= 1:
        print('A* search complete: Solution = %s with cost = %.2f' % (currentState.getPath(), currentState.gOfState()))
        print('No of nodes expanded = %d' % openList.getExpandedStatesCount())
    return currentState 


if __name__ == '__main__':
    #Test the A*search
    tspData = TSPData('/Users/apple/Documents/Projects/randTSP/10/instance_10.txt')
    print('Testing A*search on the below data')
    tspData.summary()
    tspHelper = TSPHelper(tspData)
    tspHelper.setStartCity('A')
    initialState = TSPState(tspHelper,'A')
    openList = TSPOpenList()
    closedList = TSPClosedList()
    goalState = AstarSearch(initialState, openList, closedList, verbose=1)
    print('Tour for the salesman = %s with distance = %.2f units' % (goalState.getPath(), goalState.gOfState()))
