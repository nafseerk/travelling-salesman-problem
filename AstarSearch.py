import tsp_data
import tspHelper
import tspState
import tsp_open_list
import pprint
import tsp_closed_list


def AstarSearch(initialState, openList, closedList):
    currentState = initialState
    #print('Astar search starting with state:')
    #print(currentState.path)
    while not currentState.isGoalState(): #add openList not empty condition
        #print('Astar examining state')
        #print(currentState.path)
        successors = currentState.getSuccessors()
        for successor in successors:
            if closedList.hasState(successor) == False:
                openList.add(successor)

        #print('Open List now = ')
        #openList.print()
        chosenSuccessor = openList.getItem()
        #pp = pprint.PrettyPrinter(indent=4)
        
        #print('minimum f state value:')
        #print(chosenSuccessor.fOfState())
        currentState = currentState.moveToNextState(chosenSuccessor)
        closedList.add(chosenSuccessor)
        #print('Astar moving to nextState')
        #print(currentState.path)
        #input('Enter to continue.....')

    print("The solution is:")
    currentState.printState()
    print("The cost is: %f" % currentState.gOfState())


if __name__ == '__main__':
    tspData = tsp_data.TSPData('/Users/apple/Documents/Projects/randTSP/16/instance_10.txt')
    tspHelper = tspHelper.TSPHelper(tspData)
    tspHelper.setStartCity('A')
    initialState = tspState.TSPState(tspHelper,'A')
    openList = tsp_open_list.TSPOpenList()
    closedList = tsp_closed_list.TSPClosedList()
    AstarSearch(initialState, openList, closedList)
