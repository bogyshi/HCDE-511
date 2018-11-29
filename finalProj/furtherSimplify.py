import os
import json
import argparse
import sys
import csv
import codecs
import string as str
import collections
import numpy as np
import pandas as pd

mergeIndex = 10 # 10 is the index of the neighborhood of the crime
dateIndex=2

timeGap = 200#hours

def makeTimeFrame():
    timeFrame = list()
    startTime = 0
    counter = 0
    while(startTime+timeGap<2359):
        tempTuple=(startTime,startTime+timeGap)
        startTime+=timeGap
        counter+=1
        timeFrame.append(tempTuple)
    tempTuple=(startTime,2359)
    timeFrame.append(tempTuple)
    return timeFrame

def mergeAreas(timeFrame):
    '''
    Current idea is to go through each row of the new csv with the populations.
    The mergeIndex is going to be the data we want to merge on, ex BEAT or NEIGHBORHOOD
    Then we want to group by each YEAR and get summary statistics
    so the new rows of our csv will be the same as the past except we remove
    time occured and bin according to crime subcategory and time
    The makeTimeFrame function above will return a tuple of periods of time that will act
    as a new column for each crime subcategory, so in the end we should have
    Neighborhood1, Year, Population1, Beats included, CrimeSubcategory1 0:00->2:00 ... CrimeSubcategory1 22:00->23:59, CrimeSubcategory2...
    Neighborhood2, Year, Population2,...
    ...
    NeighborhoodN,Year, ...
    Neighborhood1, Year+1,...
    ...
    '''
    csv_file = ("/home/avanroi1/HCDE-511/finalProj/data/Crime_Data2.csv")
    newdf = pd.read_csv(csv_file,',')
    newdf.dropna()
    neighborhoodDataDict = {}
    for index, data in newdf.iterrows():
        mergeData= data[mergeIndex] #mergeIndex can either be by neighborhood, beat, block, or whatever
        occuredDate = data[dateIndex]
        yearPos = occuredDate.rfind('/')
        year = int(occuredDate[yearPos+1:])
        if(year<2008):
            pass
        else:
            if(mergeData in neighborhoodDataDict):
                neighborhoodDataDict[mergeData].append(data)
            else:
                neighborhoodDataDict[mergeData] = [data]
    for k in neighborhoodDataDict.keys():
        tempDict={}
        for v in neighborhoodDataDict[k]:
            occuredDate = data[dateIndex]
            yearPos = occuredDate.rfind('/')
            year = int(occuredDate[yearPos+1:])
            if(year in tempDict):
                pass

    print('done')
timeFrame = makeTimeFrame()
print(timeFrame)
mergeAreas(timeFrame)
