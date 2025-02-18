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

def establish_monthly_patterns():
    master = []
    for temp_item in key:
        temp_freq_list = [0]*12
        preferred_months = []
        temp_addition = []
        for cust,trans,type,item,date,quantity,price,value in data:
            if item == temp_item:
                temp_freq_list[int(date[5:7])-1] += 1
           
        augmented_list = []
        augmented_list.append(temp_freq_list[11])
        for i in range(len(temp_freq_list)):
            augmented_list.append(temp_freq_list[i])
        augmented_list.append(temp_freq_list[0])
        for i in range (len(augmented_list)-1):
            if i > 0 and augmented_list[i-1] < augmented_list[i] and augmented_list[i] > augmented_list[i+1]:
                preferred_months.append(i)
        temp_addition.append(temp_item)
        temp_addition.append(preferred_months)
        master.append(temp_addition)
        print(temp_addition)
    return master

establish_monthly_patterns()



    


