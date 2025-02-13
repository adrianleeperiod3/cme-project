import csv
import bisect 
import numpy as np
from numpy.linalg import matrix_power 
import pandas as pd
import matplotlib.pyplot as plt
from numpy import *

with open("datafull.csv") as f:
    data=[tuple(line) for line in csv.reader(f)]

key = []
for cust,trans,type,item,date,quantity,price,value in data:
    count = 0
    for i in range (len(key)):
        if key[i] == item:
            count += 1
    if count == 0:
         key.append(item)
print(f"Key: \n{key}")

masterList = []
thirty_one_day_months = [1,3,5,7,8,10,12]
thirty_day_months = [4,6,9,11]
for i in range(len(data)):
    tempDate = data[i][4]
    month_decimal = 0
    try:
        thirty_one_day_months.index(int(tempDate[5:7]))
        month_decimal = float(tempDate[8:])/32.0
    except:
        try:
            thirty_day_months.index(int(tempDate[5:7]))
            month_decimal = float(tempDate[8:])/31.0
        except:
            month_decimal = float(tempDate[8:])/29.0
    masterList.append([data[i][3], round((int(tempDate[5:7])-1+month_decimal),1)])


soybean_list = []
for i in range(len(masterList)):
    if masterList[i][0] == "Soybeans":
        soybean_list.append(masterList[i][1])


plt.hist(soybean_list,12,[0,12],False)
plt.show()

def getMaximums(list):
    maxes = []
    for i in range(len(list)-2):
        if list[i] < list[i+1] and list[i+1] > list[i+2]:
            maxes.append(i+1)
    return maxes

print(getMaximums(soybean_list))


    


