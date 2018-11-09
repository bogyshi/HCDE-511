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

def generatePlots(dataTuples):
    keys=["name","num_reviews","percent_recommended","rating","latitude","longitude","price_level","cuisine","medianIncomeForArea"]
    x=[]
    y=[]
    with open('Car Models.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(row)
                line_count += 1
            else:
                print('yuh')
                x.append(row[1])
                y.append(row[2])
                line_count += 1
    #plt.xticks(x,xlbls,rotation=90)
    plt.ylabel("horsepower")
    plt.scatter(x,y) #add clrs maybe
    fig = plt.gcf()
    #fig.set_size_inches(18.5, 10.5)
    fig.tight_layout()
    fig.savefig("testing.pdf")
    plt.show()

generatePlots(None)
print("hi")
