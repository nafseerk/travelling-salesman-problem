import closed_list
import tspState
import tspHelper
import tsp_data

class TSPClosedList(closed_list.ClosedList):

    def __init__(self):
        self.closed = []
        
    def add(self, state):
        path = '->'.join(state.path)
        self.closed.append(path)
        
    def hasState(self, state):
        try:
            path = '->'.join(state.path)
            position = self.closed.index(path)
            return True
        except ValueError:
            return False

if __name__ == '__main__':
    tspData = tsp_data.TSPData('/Users/apple/Documents/Projects/randTSP/6/instance_5.txt');
    #tspData.summary()
    tspHelper = tspHelper.TSPHelper(tspData)
    tspHelper.setStartCity('A')
    state1 = tspState.TSPState(tspHelper, 'A->B->C')
    state1.fOfState()
    state1.printState()
    state2 = tspState.TSPState(tspHelper, 'A->B->D')
    state2.fOfState()
    state2.printState()
    state3 = tspState.TSPState(tspHelper, 'A->B->E')
    state3.fOfState()
    state3.printState()
    closedList = TSPClosedList()
    closedList.add(state1)
    print(closedList.hasState(state2))
    closedList.add(state3)
    
