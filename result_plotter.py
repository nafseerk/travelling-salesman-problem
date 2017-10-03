import matplotlib.pyplot as plt
import os
import math
import numpy as np

def plotResults(xValues, yValues, version):
    #TSP execution done
    x_done = []
    y_done = []

    #TSP execution terminated
    x_stopped = []
    y_stopped = []

    print('Plotting %d data points' % len(yValues))
    for i in range(len(yValues)):
        if yValues[i] != 0:
            x_done.append(xValues[i])
            y_done.append(yValues[i])
        else:
            x_stopped.append(xValues[i])
            y_stopped.append(yValues[i])
        
    donePlot = plt.scatter(x_done, y_done)
    stoppedPlot = plt.scatter(x_stopped, y_stopped)
    plt.xlabel('# of cities')
    plt.ylabel('Log(# of nodes expanded)')
    plt.legend((donePlot, stoppedPlot),
               ('execution complete', 'did not terminate'),)
    if version == 'v1':
        plt.title('A* with Heuristic')
    elif version == 'v2':
        plt.title('A* without Heuristic')
    plt.show()
   

def extrapolateResults(xValues, yValues, version):
    
    #TSP execution done
    x_done = []
    y_done = []

    #TSP execution terminated
    x_stopped = []
    y_stopped = []

    print('Plotting %d data points' % len(yValues))
    for i in range(len(yValues)):
        if yValues[i] != 0:
            x_done.append(xValues[i])
            y_done.append(yValues[i])
        else:
            x_stopped.append(xValues[i])
            y_stopped.append(yValues[i])

    donePlot = plt.scatter(x_done, y_done)
    stoppedPlot = plt.scatter(x_stopped, y_stopped)

    # predicted the outputs for the cases where algorithm terminated
    b = estimate_coef(np.array(x_done), np.array(y_done))
    y_pred = b[0] + b[1]*np.array(xValues)
    y_pred_stopped = b[0] + b[1]*np.array(x_stopped)

    # Predicted value for 36
    predictedValueOf36 = y_pred_stopped[x_stopped.index(36)]
    print('Predicted Value of 36 = %f' % predictedValueOf36)

    # plotting the regression line and prediction values
    plt.plot(xValues, y_pred, color='black')
    predictedPlot = plt.scatter(x_stopped, y_pred_stopped)
    
    plt.xlabel('# of cities')
    plt.ylabel('Log(# of nodes expanded)')
    plt.legend((donePlot, stoppedPlot, predictedPlot),
               ('execution complete', 'did not terminate', 'predicted value'),)
    if version == 'v1':
        plt.title('A* with Heuristic')
    elif version == 'v2':
        plt.title('A* without Heuristic')
    plt.show()

def estimate_coef(x, y):
    # number of observations/points
    n = np.size(x)
 
    # mean of x and y vector
    m_x, m_y = np.mean(x), np.mean(y)
 
    # calculating cross-deviation and deviation about x
    SS_xy = np.sum(y*x - n*m_y*m_x)
    SS_xx = np.sum(x*x - n*m_x*m_x)
 
    # calculating regression coefficients
    b_1 = SS_xy / SS_xx
    b_0 = m_y - b_1*m_x
 
    return(b_0, b_1)
 
def getResults(outputRootDirectory):
    x = []
    y = []
    for root, dirs, files in os.walk(outputRootDirectory):
        for directory in dirs:
            print('Collecting data for ' + directory)
            x.append(int(directory))
            outputDirectory = os.path.join(outputRootDirectory, directory)
            y_sum = 0
            notTerminatedCount = 0
            terminatedCount = 0
            for file in os.listdir(outputDirectory):
                if file.endswith("count.txt"):
                    fullFilePath = os.path.join(os.path.join(outputRootDirectory, directory), file)
                    with open(fullFilePath, 'r') as f:
                        yValue = int(f.readline())
                        #print('yValue = %d' % yValue)
                        if (yValue == -1):
                            notTerminatedCount += 1
                        else:
                            y_sum += yValue
                            terminatedCount += 1
            if notTerminatedCount > 8:
                y.append(0)
            else:
                if y_sum == 0: y.append(0)
                else:
                    y_avg = y_sum / terminatedCount
                    print('Avg # of nodes for %s cities = %d' % (directory, y_avg))
                    y.append(math.log10(y_avg))
            print('Collected %d values for %s' % (terminatedCount + notTerminatedCount, directory))        

    return x,y


if __name__ == '__main__':
    #set version 'v1' for heuristic function and 'v2' for h(n) = 0
    version = 'v1'

    #set the path of the output data folder
    outputRootFolder = '/Users/apple/Documents/git-repos/tsp/travelling-salesman-problem/output-data-with-heuristics'
    xs,ys = getResults(outputRootFolder)
    plotResults(xs, ys, version)
    extrapolateResults(xs, ys, version)
    
