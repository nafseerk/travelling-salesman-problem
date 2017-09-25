import heapq
from open_list import OpenList
from tspState import TSPState
from tspHelper import TSPHelper
from tsp_data import TSPData

class TSPOpenList(OpenList):
    """Priority Queue implementation of OpenList used for TSP problem. Contains:
       1. heap - for storing items as a priority queue
       2. counter - represents the no of states added to OpenList. This is equal to the number of
          nodes expanded in the search tree of the TSP problem
       3. size - represents the number of items in the open list   
    """

    def __init__(self):
        self.heap = []
        self.counter = 0
        self.size = 0

    def add(self, tspState):
        self.counter += 1
        self.size += 1
        #f(state) is used as the priority. When 2 states have same priority, the state that was
        #expanded first is returned
        heapq.heappush(self.heap, (tspState.fOfState(), self.counter, tspState))
        
    def getItem(self):
        self.size -= 1
        return heapq.heappop(self.heap)[2]

    def summary(self):
        print(15*'=' + 'OpenList Summary' + 15*'=')
        print('Open List Size = %d' % self.size)
        print('No of states added to OpenList so far = %d' % self.counter)
        print('Items:')
        for item in self.heap:
            print(item[2].getPath(), end=' ')
            print('f(state)=%d' % item[2].fOfState())
        print(42*'=')


if __name__ == '__main__':
    tspData = TSPData('/Users/apple/Documents/Projects/randTSP/7/instance_5.txt');
    tspData.summary()
    tspHelper = TSPHelper(tspData)
    tspHelper.setStartCity('A')

    startState = TSPState(tspHelper, 'A')
    aState = TSPState(tspHelper, 'A->E->B->F');
    aState = startState.moveToNextState(aState)
    successors = aState.getSuccessors()

    #Testing add function
    openList = TSPOpenList()
    for successor in successors:
        openList.add(successor)
    openList.summary()

    #Testing get function - should return the state with lowest f(state)
    nextState = openList.getItem()
    print('The next state chosen is:')
    nextState.summary()
 
