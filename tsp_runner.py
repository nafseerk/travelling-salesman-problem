from tsp_data import TSPData
from tspHelper import TSPHelper
from tspState import TSPState
from tsp_open_list import TSPOpenList
from tsp_closed_list import TSPClosedList
import AstarSearch as a_star
import os

def runOnFile(inputFilePath, version, outputDirectory):
    #If the tsp was already solved quit
    filePath = os.path.join(outputDirectory, os.path.splitext(os.path.basename(os.path.normpath(inputFilePath)))[0])
    solutionFilePath = filePath + '_result.txt'
    countFilePath = filePath + '_count.txt'
    if os.path.exists(solutionFilePath) and os.path.exists(countFilePath): return

    ##Solve the tsp and store the solution and nodes count in file
    tspData = TSPData(inputFilePath)
    if version == 'v1':
        tspHelper = TSPHelper(tspData)
    elif version == 'v2':
        tspHelper = TSPHelper(tspData, noHeuristic=True)
    tspHelper.setStartCity('A')
    initialState = TSPState(tspHelper,'A')
    openList = TSPOpenList()
    closedList = TSPClosedList()
    goalState = a_star.AstarSearch(initialState, openList, closedList)
    with open(solutionFilePath, 'w') as f:
        if goalState != None:
            tspData.summary(file=f)
            print('Tour for the salesman = %s with distance = %.2f units' % (goalState.getPath(), goalState.gOfState()), file=f)
            print('Number of nodes expanded: %d' % openList.getExpandedStatesCount(), file=f)
        else:
            tspData.summary(file=f)
            print('No solution found', file=f)
    with open(countFilePath, 'w') as f:
        if goalState == None:
             print(-1, file=f)
        else:
            print(openList.getExpandedStatesCount(), file=f)

def runOnDataSet(inputRootDirectory, version):
    outputRootDirectory = os.path.join(os.path.abspath(os.path.join(inputRootDirectory, os.pardir)), 'output-data-' + version)
    if not os.path.exists(outputRootDirectory):
        os.makedirs(outputRootDirectory)

    for root, dirs, files in os.walk(inputRootDirectory):
        for directory in dirs:
            outputDirectory = os.path.join(outputRootDirectory, directory)
            if not os.path.exists(outputDirectory): os.makedirs(outputDirectory)
            for file in os.listdir(os.path.join(inputRootDirectory, directory)):
                if file.endswith(".txt"):
                    fullFilePath = os.path.join(os.path.join(inputRootDirectory, directory), file)
                    if version == 'v1':
                        print('A* search on %s cities: %s started' % (directory, file))
                        runOnFile(fullFilePath, version ,  outputDirectory)
                        print('A* search on %s cities: %s completed' % (directory, file))
                    elif version == 'v2':
                        print('A* search with no heuristic on %s cities: %s started' % (directory, file))
                        runOnFile(fullFilePath, version,  outputDirectory)
                        print('A* search with no heuristic on %s cities: %s completed' % (directory, file))
                    

#set path of input data here        
inputRootDirectory = '/Users/apple/Documents/git-repos/tsp/travelling-salesman-problem/input-data'

#'v1' for search with heuristic and 'v2' for heuristic h(n) = 0
version = 'v1'
runOnDataSet(inputRootDirectory, version)
