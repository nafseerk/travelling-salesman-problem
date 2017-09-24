import tsp_data

class TSPHelper:

    def __init__(self, tspData):
        self.tspData = tspData
        self.visitedCities = set()
        self.unvisitedCities = set(tspData.getAllCities())
        self.startCity = None
        self.nextCity = None

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

    def setNextCity(self, city):
        self.nextCity = city

    def getNextCity(self):
        return self.nextCity


if __name__ == '__main__':
    tspData = tsp_data.TSPData('/Users/apple/Documents/Projects/randTSP/6/instance_5.txt');
    tspData.summary()
    tspHelper = TSPHelper(tspData)
    print(tspHelper.getVisitedCities())
    print(tspHelper.getUnvisitedCities())
    tspHelper.visitCity('A')
    print(tspHelper.getVisitedCities())
    print(tspHelper.getUnvisitedCities())


