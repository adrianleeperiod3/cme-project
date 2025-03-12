import csv
import bisect 
import numpy as np
from numpy.linalg import matrix_power 
import pandas as pd
import matplotlib.pyplot as plt

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

def establish_monthly_patterns():
    master = []
    for temp_item in key:
        t = freq_list(temp_item)
           
        preferred_months = []
        temp_addition = []
        augmented_list = []
        augmented_list.append(t[11])
        for i in range(len(t)):
            augmented_list.append(t[i])
        augmented_list.append(t[0])
        for i in range (len(augmented_list)-1):
            if i > 0 and augmented_list[i-1] < augmented_list[i] and augmented_list[i] > augmented_list[i+1]:
                preferred_months.append(i)
        temp_addition.append(temp_item)
        temp_addition.append(preferred_months)
        master.append(temp_addition)
    return master

def freq_list(input_item):
    list = [0]*12
    for cust,trans,type,item,date,quantity,price,value in data:
        if item == input_item:
            list[int(date[5:7])-1] += 1
    return list


    


