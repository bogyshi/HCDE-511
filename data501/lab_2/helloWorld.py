from urllib.request import Request, urlopen, URLError
import json
import re
import pickle
import string
import matplotlib.pyplot as plt
import os.path
import numpy as np

#import texttable as tt
import csv

print("helloWorld")
germanCarMods=['Audi', 'BMW', 'Mercedes-Benz', 'Porsche', 'Volkswagen']
params = ['Vehicle Name', 'Engine Size', 'Cyl', 'HP', 'City MPG', 'Hwy MPG', 'Weight', 'Wheel Base', 'Len', 'Width']
def createGermanCSVs():
    with open('data_car_2004.csv') as car_file:
        car_reader = csv.reader(car_file,delimiter=',')
        headers = next(car_reader,None)
        for x in headers:
            if x == params[0]:
                pass
        print(headers)
        for row in car_reader:
            temp = list()
            carMod = row[0].rsplit(" ")[0]
            if(carMod in germanCarMods):
                temp.append(row)
                newData.append(row)
    print(newData)
    newData = [headers]+newData
    with open('german_car.csv',"w") as f:
        writer = csv.writer(f)
        writer.writerows(newData)

def createnetprofitCSVs():
    newData = list()
    with open('data_car_2004.csv') as car_file:
        car_reader = csv.reader(car_file,delimiter=',')
        headers = next(car_reader,None)+['Net']
        for row in car_reader:
            netprofit = ((int(row[9]) - int(row[10]))/float(row[9]))*100
            newData.append(row+[str(netprofit)])
    newData = [headers]+newData
    with open('profit_car.csv',"w") as f:
        writer = csv.writer(f,delimiter='\t')
        writer.writerows(newData)

createnetprofitCSVs()
