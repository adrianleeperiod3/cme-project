import csv
import bisect 
import numpy as np
from numpy.linalg import matrix_power 

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
    if thirty_one_day_months.index(int(tempDate[5:7])) != -1:
        month_decimal = float(tempDate[8:])/31.0

    


