import state
import tsp_data
import tspHelper

class TSPState(state.State):

    def __init__(self, tspHelper, path):
        self.tspHelper = tspHelper
        self.path = path.split('->')
        self.g = -1
        self.h = -1
        self.f = -1

    def isGoalState(self):
        return self.path[0] == self.tspHelper.startCity and \
               self.path[0] == self.path[-1] and \
               set(self.path[0:-1]) == set(self.tspHelper.tspData.getAllCities())

    def moveToNextState(self):
        nextCity = self.tspHelper.getNextCity()
        nextPath = '->'.join(self.path)
        nextPath += '->' + nextCity
        self.tspHelper.visitCity(nextCity)
        return TSPState(self.tspHelper, nextPath)

    def getSuccessors(self):
        successorsList = []
        unvisitedCitiesList = list(self.tspHelper.getUnvisitedCities())
        
        for unvisited in unvisitedCitiesList:
            successorPath = '->'.join(self.path)
            successorPath += '->' + unvisited
            successorsList.append(TSPState(self.tspHelper, successorPath))

        if not unvisitedCitiesList:
            successorPath = '->'.join(self.path)
            successorPath += '->' + self.tspHelper.getStartCity()
            successorsList.append(TSPState(self.tspHelper, successorPath))
            
        minimumF = 999999
        minSuccessor = None
        for successor in successorsList:
            if successor.fOfState() < minimumF:
                minimumF = successor.fOfState()
                minSuccessor = successor
                
        if minSuccessor != None:
            self.tspHelper.setNextCity(minSuccessor.path[-1])

        return successorsList


    def gOfState(self):
        if self.g == -1:
            pathCost = 0
            for i in range(len(self.path) - 1):
                pathCost += self.tspHelper.tspData.getDistance(self.path[i], self.path[i+1])
            self.g = pathCost
        return self.g

    def hOfState(self):
        #hOfState = 1. distanceToNearestUnvisited + 2. mstPathCost (of unvisited cities) + 3. distanceBackToStart
        if self.h == -1:
            unvisitedCitiesList = list(self.tspHelper.getUnvisitedCities())
            if len(unvisitedCitiesList) == 0:
                self.h = 0
                return 0
            
            #1. Get the distance from current city to nearest unvisited city
            currentCity = self.path[-1]
            distanceToNearestUnvisited = 0
            for unvisited in unvisitedCitiesList:
                dist = self.tspHelper.tspData.getDistance(currentCity, unvisited)
                if dist < distanceToNearestUnvisited:
                    distanceToNearestUnvisited = dist

            #2. Get the cost of the minimum spanning tree of remaining unvisited cities
            mstPathCost = self.tspHelper.tspData.getMinimumSpanningTreeCost(unvisitedCitiesList, unvisitedCitiesList[0])

            #3. Get the nearest distance to start city from univisited city
            distanceBackToStart = 0
            for unvisited in unvisitedCitiesList:
                dist = self.tspHelper.tspData.getDistance(self.tspHelper.startCity, unvisited)
                if dist < distanceBackToStart:
                    distanceBackToStart = dist

        self.h = distanceToNearestUnvisited + mstPathCost + distanceBackToStart
        return self.h
            
    def fOfState(self):
        if self.f == -1:
            self.f = self.gOfState() + self.hOfState()
        return self.f

    def printState(self):
        print("State = %s" % '->'.join(self.path))
        print('g = %d; h = %d; f = %d' % (self.g, self.h, self.f))

if __name__ == '__main__':
    tspData = tsp_data.TSPData('/Users/apple/Documents/Projects/randTSP/6/instance_5.txt');
    tspData.summary()
    tspHelper = tspHelper.TSPHelper(tspData)
    tspHelper.setStartCity('A')
    aState = TSPState(tspHelper, 'A->B->C->D->E->F->A')
    print(aState.gOfState())
    tspHelper.visitCity('A')
    tspHelper.visitCity('B')
    tspHelper.visitCity('C')
    aState.printState()
    for successor in aState.getSuccessors():
        successor.printState()

    print(tspHelper.getNextCity())
