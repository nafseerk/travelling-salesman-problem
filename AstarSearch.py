import tsp_data
import tspHelper
import tspState


def AstarSearch(initialState):
    currentState = initialState
    print('Astar search starting with state:')
    print(currentState.path)
    while not currentState.isGoalState(): #add openList not empty condition
        print('Astar examining state')
        print(currentState.path)
        successors = currentState.getSuccessors()
        #if any of the successors in closed list remove them
        #add the successors to open list
        minimumF = 999999
        minSuccessor = None
        for successor in successors:
            if successor.fOfState() < minimumF:
                minimumF = successor.fOfState()
                minSuccessor = successor

        currentState = currentState.moveToNextState()
        print('Astar moving to nextState')
        print(currentState.path)

    print("The solution is:")
    currentState.printState()
    print("The cost is: %d" % currentState.gOfState())


if __name__ == '__main__':
    tspData = tsp_data.TSPData('/Users/apple/Documents/Projects/randTSP/problem36')
    tspHelper = tspHelper.TSPHelper(tspData)
    tspHelper.setStartCity('A')
    initialState = tspState.TSPState(tspHelper,'A')
    AstarSearch(initialState)
