import heapq
import open_list
import tspState
import tspHelper
import tsp_data

class TSPOpenList(open_list.OpenList):

    def __init__(self):
        self.heap = []
        self.counter = 0

    def add(self, tspState):
        self.counter += 1
        heapq.heappush(self.heap, (tspState.fOfState(), self.counter, tspState))
        
    def getItem(self):
        return heapq.heappop(self.heap)[2]

    def print(self):
        print('Open List Size = %d' % self.counter)
        for item in self.heap:
            print(item[2].path)


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
    openList = TSPOpenList()
    openList.add(state1)
    openList.add(state2)
    openList.add(state3)
    minState = openList.getItem()
    minState.printState()
