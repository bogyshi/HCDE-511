import os
import json
import argparse
import sys
import csv
import codecs
import string as str
print("hullo")
import collections
import numpy as np
import pandas as pd

otherTracts = set()
handleMore = True
def grabUniqueNeighborhoods(x):
    neighborhoodIndex = 10
    csv_file = ("/home/avanroi1/HCDE-511/finalProj/data/Crime_Data.csv")
    csv_reader = csv.reader(open(csv_file,'rb'), delimiter=',')
    crimeNeighbors = {}
    crimeNeighbors2 = {}
    didntMakeit=set()
    header = next(csv_reader)
    for row in csv_reader:
        name = row[neighborhoodIndex]
        if(handleMore is True):
            if(name == "UNIVERSITY"):
                name = "UNIVERSITY DISTRICT"
            elif(name == "NEW HOLLY"):
                name = "NEWHOLLY"
            elif(name == "NORTH ADMIRAL"):
                name = "ADMIRAL"
            elif("MOUNT BAKER" in name):
                name = "MT. BAKER"
            elif("LAKECITY" in name):
                name = "LAKE CITY"
            elif(name == "FAUNTLEROY SW"):
                name = "FAUNTLEROY"
            elif(name == "MORGAN"):
                name = "MORGAN JUNCTION"
            elif("MADRONA" in name):
                name = "MADRONA"
            elif("PORTAGE BAY" in name):
                name = "PORTAGEBAY"
            elif("HARBOR ISLAND" in name):
                name = "HARBOR ISLAND"
            elif("SQUIRE PARK" in name):
                name = "SQUIRE PARK"
            elif("DUWAMISH" in name):
                name = "DUWAMISH"
            elif(name == "SANDPOINT"):
                name = "SAND POINT"
            elif(name == "BITTERLAKE"):
                name = "BITTER LAKE"
            elif("BALLARD" in name):
                name = "BALLARD"
            elif("BEACON HILL" in name):
                name = "BEACON HILL"
            elif("EASTLAKE" in name):
                name = "EASTLAKE"
            elif("CASCADE" in name):
                name = "CASCADE"
            elif("RAVENNA" in name):
                name = "RAVENNA"
            elif("LAKEWOOD" in name):
                name = "LAKEWOOD"
            elif("DUNLAP" in name):
                name = "DUNLAP"
            elif("WESTWOOD" in name):
                name = "WESTWOOD"
            elif("DOWNTOWN COMMERCIAL" in name):
                name = "DOWNTOWN COMMERCIAL CORE"
            elif("CHINATOWN/INTERNATIONAL DISTRICT" in name):
                name = "CHINATOWN-INTERNATIONAL DISTRICT"
        if(name not in crimeNeighbors):
            crimeNeighbors[name] = 1
        else:
            crimeNeighbors[name] += 1
        if(name in x.keys()):
            crimeNeighbors2[name] = x[name]
        else:
            didntMakeit.add(row[neighborhoodIndex])
    print("Not in the resulting data yet")
    print(didntMakeit)
    return crimeNeighbors2

def grabUniqueCensusTract():
    neighborhoodIndex = 13
    tractIndex = 3
    csv_file = ("/home/avanroi1/HCDE-511/finalProj/data/SeattleCensusBlocksandNeighborhoodCorrelationFile.csv")
    csv_reader = csv.reader(open(csv_file,'rb'), delimiter=',')
    neighborHoodTractDict = {}
    header = next(csv_reader)
    for row in csv_reader:
        otherTracts.add(row[0][:-4])
        someval = int(row[0][:-4])
        areas = str.upper(row[neighborhoodIndex]).rsplit(',')
        areas = [x.strip(' ') for x in areas]
        for a in areas:
            if(a not in neighborHoodTractDict):
                neighborHoodTractDict[a] = set()
                neighborHoodTractDict[a].add(someval)
            else:
                neighborHoodTractDict[a].add(someval)
    return neighborHoodTractDict

def grabTracts(y):
    geoIndex=1
    popIndex=3
    endIndex = 21
    csv_file = ("/home/avanroi1/HCDE-511/finalProj/data/populationEstimates.csv")
    csv_reader = csv.reader(open(csv_file,'rb'), delimiter=',')

    tracts = set()
    pops={}
    df = pd.DataFrame()
    yearIndex=popIndex
    while yearIndex <= endIndex:
        csv_reader = csv.reader(open(csv_file,'rb'), delimiter=',')
        header = next(csv_reader)
        print(header)
        for x in y.keys():
            pops[x] = 0
        for row in csv_reader:
            for key,val in y.iteritems():
                for geoCode in val:
                    if(geoCode == int(row[geoIndex])):
                        pops[key]=pops[key]+int(row[yearIndex])
                        #print("wemadeit")

        df=df.append(pd.Series(pops),ignore_index=True)
        yearIndex=yearIndex+1
            #tracts.add(row[geoIndex])
    return df

def makeNewCSV(df):
    neighborhoodIndex = 10
    yearIndex=1
    csv_file = ("/home/avanroi1/HCDE-511/finalProj/data/Crime_Data.csv")
    csv_reader = csv.reader(open(csv_file,'rb'), delimiter=',')
    newdf = pd.read_csv(csv_file,',')
    newdf["pop"]=np.nan
    numEntries = len(newdf.index)
    pops = np.full(numEntries, np.nan)
    yearMax=2018
    yearMin=2000
    print(newdf.head(3))
    for index, row in newdf.iterrows():
        name = row[neighborhoodIndex]
        if(handleMore is True):
            if(name == "UNIVERSITY"):
                name = "UNIVERSITY DISTRICT"
            elif(name == "NEW HOLLY"):
                name = "NEWHOLLY"
            elif(name == "NORTH ADMIRAL"):
                name = "ADMIRAL"
            elif(name == "MOUNT BAKER"):
                name = "MT.BAKER"
            elif(name == "FAUNTLEROY SW"):
                name = "FAUNTLEROY"
            elif(name == "MORGAN"):
                name = "MORGAN JUNCTION"
            elif("MADRONA" in name):
                name = "MADRONA"
            elif("PORTAGE BAY" in name):
                name = "PORTAGEBAY"
            elif("HARBOR ISLAND" in name):
                name = "HARBOR ISLAND"
            elif("SQUIRE PARK" in name):
                name = "SQUIRE PARK"
            elif("DUWAMISH" in name):
                name = "DUWAMISH"
            elif(name == "SANDPOINT"):
                name = "SAND POINT"
            elif(name == "BITTERLAKE"):
                name = "BITTER LAKE"
            elif("BALLARD" in name):
                name = "BALLARD"
            elif("BEACON HILL" in name):
                name = "BEACON HILL"
            elif("EASTLAKE" in name):
                name = "EASTLAKE"
            elif("CASCADE" in name):
                name = "CASCADE"
            elif("RAVENNA" in name):
                name = "RAVENNA"
            elif("LAKEWOOD" in name):
                name = "LAKEWOOD"
            elif("DUNLAP" in name):
                name = "DUNLAP"
            elif("WESTWOOD" in name):
                name = "WESTWOOD"
            elif("DOWNTOWN COMMERCIAL" in name):
                name = "DOWNTOWN COMMERCIAL CORE"
            elif("CHINATOWN/INTERNATIONAL DISTRICT" in name):
                name = "CHINATOWN-INTERNATIONAL DISTRICT"
        if(name in df.columns.values):
            whichCol = df.columns.get_loc(name)
            year = int(row[yearIndex].rsplit('/')[2])
            if(year<=yearMax and year>=yearMin):
                pops[index] = df.iloc[year-yearMin,whichCol]

        #if(row[neighborhoodIndex] in list(df.columns.values))
    newdf["pop"]=pops
    return newdf

print os.getcwd()
x = grabUniqueCensusTract()
dx = collections.OrderedDict(sorted(x.items()))
print(dx)

y = grabUniqueNeighborhoods(x)
dy= collections.OrderedDict(sorted(y.items()))
print(y)
result = grabTracts(y)
print(result)
print(result.sum(axis=1))
done = makeNewCSV(result)
done.to_csv("/home/avanroi1/HCDE-511/finalProj/data/Crime_Data2.csv",",")
