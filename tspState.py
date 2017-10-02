import state
from tsp_data import TSPData
from tspHelper import TSPHelper

class TSPState(state.State):
    """Subclass representing a state of the TSP problem. Contains attributes:
       1. tspHelper - all TSPState objects share the same instance of tspHelper object
       2. path - This is the how a state is represented - an ordered list of cities that represents a tour
                 Note that a TSPState is represented by a tour rather than a single city. The current city of the tour is
                 the last city of the path
       3. g - represents cost of the tour represented by the TSPState
       4. h - represents heuristic function of the tour represented by the TSPState
              h(tspState) = d1 + d2( mstCost of remaining unvisited cities) + d3
                            where d1 = Distance from the current city of the tour to the nearest unvisited city
                                  d2 = The Cost of the Minimum Spanning Tree formed by all the unvisited cities
                                  d3 = Shortedt distance from one of the unvisited cities back to the start city
       5. f - is g + h
    """

    def __init__(self, tspHelper, path):
        """ Create  a TSPState. Takes 1. the tspHelper instance of the problem and
            2. a string representing path in the format A->B->C->D
        """
        self.tspHelper = tspHelper
        self.path = path.split('->')
        self.g = -1
        self.h = -1
        self.f = -1

    def getPath(self):
        return '->'.join(self.path)
    
    def isGoalState(self):
        """Checks if starts and ends at the same city and has visited all the other cities exactly once"""
        return self.path[0] == self.tspHelper.startCity and \
               self.path[0] == self.path[-1] and \
               sorted(self.path[0:-1]) == sorted(self.tspHelper.tspData.getAllCities())

    def moveToNextState(self, nextState):
        """Takes the necessary step to move from current state to the nextState"""
        nextPath = '->'.join(nextState.path)
        self.tspHelper.updateVisitedCities(nextState.path)
        return nextState

    def getSuccessors(self):
        """Returns a list of States representing the successors of the current.
           A successor of the current state is formed by adding a single unvisited city
           to the tour represented by the current state 
        """

        #No successors for a goal state
        if self.isGoalState(): 
            return []
        
        successorsList = []
        unvisitedCitiesList = list(self.tspHelper.getUnvisitedCities())
        
        for unvisited in unvisitedCitiesList:
            successorPath = '->'.join(self.path)
            successorPath += '->' + unvisited
            successorsList.append(TSPState(self.tspHelper, successorPath))

        #If there are no unvisitedCities left then go back to the startCity
        if not unvisitedCitiesList:
            successorPath = '->'.join(self.path)
            successorPath += '->' + self.tspHelper.getStartCity()
            successorsList.append(TSPState(self.tspHelper, successorPath))

        return successorsList


    def gOfState(self):
        if self.g == -1:
            pathCost = 0
            for i in range(len(self.path) - 1):
                pathCost += self.tspHelper.tspData.getDistance(self.path[i], self.path[i+1])
            self.g = pathCost
        return self.g

    def hOfState(self):
        if self.tspHelper.noHeuristic == False:
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
        else: return 0
            
    def fOfState(self):
        if self.f == -1:
            self.f = self.gOfState() + self.hOfState()
        return self.f

    def summary(self):
        print(15*'=' + "State Summary" + 15*'=')
        print("Tour = %s" % '->'.join(self.path))
        self.fOfState()
        print('g = %d; h = %d; f = %d' % (self.g, self.h, self.f))
        print(42*'=')

if __name__ == '__main__':
    tspData = TSPData('/Users/apple/Documents/Projects/randTSP/10/instance_10.txt');
    tspData.summary()
    tspHelper = TSPHelper(tspData)
    tspHelper.setStartCity('A')


    startState = TSPState(tspHelper, 'A')
    print('\nThis is the initial state')
    startState.summary()

    #An intermediate state of the TSP problem
    aState = TSPState(tspHelper, 'A->E->I->C->F');
    aState = startState.moveToNextState(aState)
    print('\nThis is an intermediate state')
    print('Is %s a goal state ? %r ' % (aState.getPath(), aState.isGoalState()))
    aState.summary()

    #Find all the successors of the state
    successors = aState.getSuccessors()
    print('The state %s has following successors:' % '->'.join(aState.path))
    for successor in successors:
        print(successor.getPath())

    #Goal state has heuristic value as 0 and no successors
    aGoalState = TSPState(tspHelper, 'A->E->I->C->F->D->J->G->H->B->A')
    aGoalState = aState.moveToNextState(aGoalState)
    print('\nThis is an intermediate state')
    print('Is %s a goal state ? %r ' % (aGoalState.getPath(), aGoalState.isGoalState()))
    aGoalState.summary()
    successors = aGoalState.getSuccessors()
    print('No of successors for a goal state = %d' % len(successors))
    


    
