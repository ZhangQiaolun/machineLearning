from math import log

# Is it good enough? only calculate the ShannonEnt for the type, what if the feature is the same and dif
def calcShannonEnt(dataSet):
    numEntries = len(dataSet)
    labelCounts = {}
    for featVec in dataSet:
        currentLabel = featVec[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
    shannonEnt = 0.0
    for key in labelCounts:
        prob = float(labelCounts[key])/numEntries
        shannonEnt -= prob * log(prob, 2)
    return shannonEnt

def createDataSet():
    dataSet = [[1, 1, 'yes'],
               [1, 0, 'yes'],
               [1, 0, 'no'],
               [0, 1, 'no'],
               [0, 1, 'no']]
    labels = ['no surfacing', 'flippers']
    return dataSet, labels

# dataSet is the dataSet to be divided
# axis is the feature used to divide the dataSet
# value is the dataSet to reutrn
def splitDataSet(dataSet, axis, value):
    retDataSet = []
    for featVec in dataSet:
        if

