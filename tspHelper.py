from tsp_data import TSPData

class TSPHelper:
    """Helper class for carrying out book keeping tasks related to TSP problem.
       Also contains utility functions. Has attributes
       1. tspData - tspData instance of the specific TSP problem
       2. visitedCities - list of visited cities of the current tour
       3. unvisitedCities - list of unvisited cities of the current tour
       4. startCity - starting city of the tour which is also the last city of the tour
    """

    #TODO - should have an attribute for the current tour
    def __init__(self, tspData, noHeuristic=False):
        self.tspData = tspData
        self.visitedCities = set()
        self.unvisitedCities = set(tspData.getAllCities())
        self.startCity = None
        self.noHeuristic = noHeuristic

    def getVisitedCities(self):
        return self.visitedCities

    def getUnvisitedCities(self):
        return self.unvisitedCities

    def visitCity(self, city):
        self.visitedCities.add(city)
        self.unvisitedCities.discard(city)

    def setStartCity(self, city):
        self.startCity = city
        self.visitCity(city)

    def getStartCity(self):
        return self.startCity

    def updateVisitedCities(self, tour):
        """Given a tour represented by tour, update visitedCities and unvisitedCities"""
        self.visitedCities = set(tour)
        self.unvisitedCities = set(self.tspData.getAllCities())
        for city in self.visitedCities:
            self.unvisitedCities.discard(city)
        

if __name__ == '__main__':
    tspData = TSPData('/Users/apple/Documents/Projects/randTSP/6/instance_5.txt');
    tspData.summary()
    print('List of cities', end=' ')
    print(tspData.getAllCities())

    #Show the visited and unvisited cities given a tour
    tour = ['A', 'D', 'E', 'C']
    print('Current Tour = ' + '->'.join(tour))
    tspHelper = TSPHelper(tspData)
    tspHelper.setStartCity('A') #TODO: move setStartCity inside the constructor
    tspHelper.updateVisitedCities(tour)
    print('Visited cities =', end=' ')
    print(tspHelper.getVisitedCities())
    print('Unvisited cities =', end=' ')
    print(tspHelper.getUnvisitedCities())

    #Visit a new city
    print('After visting city B:')
    tspHelper.visitCity('B')
    print('Visited cities =', end=' ')
    print(tspHelper.getVisitedCities())
    print('Unvisited cities =', end=' ')
    print(tspHelper.getUnvisitedCities())

