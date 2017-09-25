from closed_list import ClosedList
from tspState import TSPState
from tspHelper import TSPHelper
from tsp_data import TSPData

class TSPClosedList(ClosedList):
    """Implementation of closed list for tsp problem. Contains
       1. closed - list of states
       2. size - no of states in closed list
    """

    def __init__(self):
        self.closed = []
        self.size = 0
        
    def add(self, state):
        path = '->'.join(state.path)
        self.closed.append(path)
        self.size += 1
        
    def hasState(self, state):
        """Returns True if the state was already evaluated by the search problem. Else return False"""
        try:
            path = '->'.join(state.path)
            position = self.closed.index(path)
            return True
        except ValueError:
            return False

    def summary(self):
        print(15*'=' + 'ClosedList Summary' + 15*'=')
        print('Closed List Size = %d' % self.size)
        print('Items:')
        for item in self.closed:
            print(item)
        print(42*'=')

if __name__ == '__main__':
    tspData = TSPData('/Users/apple/Documents/Projects/randTSP/6/instance_5.txt');
    tspData.summary()
    tspHelper = TSPHelper(tspData)
    tspHelper.setStartCity('A')

    #Testing add method
    state1 = TSPState(tspHelper, 'A->B->C')
    state2 = TSPState(tspHelper, 'A->B->D')
    state3 = TSPState(tspHelper, 'A->B->E')
    closedList = TSPClosedList()
    closedList.add(state1)
    closedList.add(state2)
    closedList.add(state3)
    closedList.summary()

    #Testing hasState function
    testState1 = TSPState(tspHelper, 'A->B->C')
    testState2 = TSPState(tspHelper, 'A->B->F')
    print('Is state %s closed? %r' % (testState1.getPath(), closedList.hasState(testState1)))
    print('Is state %s closed? %r' % (testState2.getPath(), closedList.hasState(testState2)))
    
    
