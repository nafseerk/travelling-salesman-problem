import math
from tabulate import tabulate
import itertools
import pprint

class TSPData:
    citiesCount = 0
    citiesCoordinates = {}
    
    def __init__(self, inputFileName):
        f = open(inputFileName, 'r') 
        lines = f.readlines()
        f.close()
        
        self.citiesCount=int(lines[0])

        for line in lines[1:]:
            cityId, cityX, cityY = line.split(' ') 
            self.citiesCoordinates[cityId] = (int(cityX), int(cityY))

        return


    def getDistance(self, city1Id, city2Id):
        #TODO: incorportate float
        x1, y1 = self.citiesCoordinates[city1Id]
        x2, y2 = self.citiesCoordinates[city2Id]
        return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

    def getAllCities(self):
        return list(self.citiesCoordinates.keys())
        
    def summary(self):
        print('No of cities = %d' % self.citiesCount)
        headers = ['CityId', 'X-coordinate', 'Y-coordinate']
        data = sorted([(k,v[0],v[1]) for k,v in self.citiesCoordinates.items()])
        print(tabulate(data, headers=headers))

    def getMinimumSpanningTreeCost(self, citiesList, startCity):
        pp = pprint.PrettyPrinter(indent=4)
        if len(citiesList) == 0:
            return 0

        #print('Calling MST with startCity ', startCity, ' on')
        #print(citiesList)
        
        if startCity not in citiesList:
            print('StartCity should be in the cities list')

        #find the distances of all combinations of cities
        paths = [(path[0], path[1], self.getDistance(path[0], path[1])) for path in itertools.combinations(citiesList, 2)]
        paths.sort(key=lambda tup: tup[2])
        #print('printing all paths')
        #pp.pprint(paths)
        
        mstSoFar = [startCity]
        mstPathCost = 0
        del citiesList[citiesList.index(startCity)]

        while citiesList:
            #print('mstSoFar = ')
            #print(mstSoFar)
            #from all possible city pairs take only those that connect a city from mstSoFar to a city not in mstSoFar
            filteredPaths = []
            for path in paths:
                if (path[0] in mstSoFar and path[1] not in mstSoFar) or (path[1] in mstSoFar and path[0] not in mstSoFar):
                    filteredPaths.append(path)                   
            filteredPaths = sorted(filteredPaths, key=lambda tup: tup[2])
            #print('filtered paths = ')
            #pp.pprint(filteredPaths)
            nextPath = filteredPaths.pop(0)
            #print('nextpath = ')
            #pp.pprint(nextPath)
            if (nextPath[0] in mstSoFar) and (nextPath[1] not in mstSoFar):
                nextCity = nextPath[1]
            elif (nextPath[1] in mstSoFar) and (nextPath[0] not in mstSoFar):
                nextCity = nextPath[0]
            mstPathCost += nextPath[2]
            mstSoFar.append(nextCity)
            #print('nextCity from mst = ' + nextCity)
            del citiesList[citiesList.index(nextCity)]
            paths = [path for path in paths if path != nextPath]
            #print('after removing the selected path')
            #pp.pprint(paths)
        return mstPathCost
                    
if __name__ == '__main__':
    cities = TSPData('/Users/apple/Documents/Projects/randTSP/4/instance_3.txt')
    cities.summary()
    #print("distance from A to B = %d" % cities.getDistance('A', 'B'))
    print(cities.getMinimumSpanningTreeCost(cities.getAllCities(), 'A'))
    #print(cities.getAllCities())
