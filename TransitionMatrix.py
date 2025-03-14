import csv
import bisect 
import numpy as np
from numpy.linalg import matrix_power 
import statistics
from datetime import datetime

with open("datafull.csv") as f:
    data=[tuple(line) for line in csv.reader(f)]

ordered_transactions = [] #orders objects with respect to transaction number
t_b_c = [] #orders purchased-item objects by individual users
key = []

for cust,trans,type,item,date,quantity,price,value in data:
    count = 0
    for i in range (len(key)):
        if key[i] == item:
            count += 1
    if count == 0:
        key.append(item)
        
def extract_int(str): #pulls an int out of a given string
    r = []
    for i in str:
        if i.isdigit():
            r.append(i)
    return int(''.join(r))

def occurances(int): #counts the occurances of a given int within ordered_transactions
    occurances = 0
    for i in range(len(ordered_transactions)):
        if ordered_transactions[i][0] == int:
            occurances += 1
    return occurances

def days_between_dates(date1_str, date2_str):
    date1 = datetime.strptime(date1_str, "%Y-%m-%d")
    date2 = datetime.strptime(date2_str, "%Y-%m-%d")
    d = ((date2 - date1).days)
    return d 

def order_by_date(): #orders transaction objects by sequential dates
    tempList = []
    n = 0
    for cust,trans,type,item,date,quantity,price,value in data:
        if len(tempList) == 0:
            ordered_transactions.append([extract_int(cust),item,date])
        else:
            i = 0
            while days_between_dates(tempList[i][3],date) <= 0:
                i += 1
            tempList.insert([extract_int(cust),item,date],i)
        
def transactions_by_customer(): #creates an array to order each individuals sequential transactions
    cust_blacklist = []
    for i in range (len(ordered_transactions)):
        temp_cust = ordered_transactions[i][0]
        if occurances(temp_cust) == 1:
            t_b_c.append([[ordered_transactions[i][1],ordered_transactions[i][2]]])
        else:
            tempItems = []
            for j in range (len(ordered_transactions)):
                if ordered_transactions[j][0] == temp_cust and temp_cust not in cust_blacklist:
                    tempItems.append([ordered_transactions[j][1],ordered_transactions[j][2]])
            if len(tempItems) != 0:
                t_b_c.append(tempItems)
                cust_blacklist.append(temp_cust)
    
def three_sigma_rule():
    l = []
    index_to_split = []
    for n in range(len(t_b_c)):
        purchase_intervals = []
        temp_splits = []
        for i in range(len(t_b_c[n])-1):
            purchase_intervals.append(days_between_dates(t_b_c[n][i][1],t_b_c[n][i+1][1]))
        if len(purchase_intervals) > 1:
            upper_limit = statistics.mean(purchase_intervals) + statistics.stdev(purchase_intervals)
        for i in range(len(purchase_intervals)):
            if purchase_intervals[i] > upper_limit:
                temp_splits.append(i)
            index_to_split.append(temp_splits)
    for i in range(len(t_b_c)):
        temp_list = []
        temp_cust = t_b_c[i]
        for j in range(len(temp_cust)):
            if j not in index_to_split[i]:
                temp_list.append(temp_cust[j][0])
            else:
                temp_list.append(temp_cust[j][0])
                if len(temp_list) > 1:
                    l.append(temp_list)
                temp_list = []
            if j == len(temp_list) and len(temp_list) > 1:
                l.append(temp_list)
                temp_list = []
    return l

def create_Transition_Matrix(): #creates the Markov Matrix
    order_by_date()
    transactions_by_customer()
    t_b_c = three_sigma_rule()
    
    matrix = np.zeros([len(key),len(key)], dtype = float)
    state_count = [0] * len(key)
    for i in range (len(t_b_c)):
        for j in range((len(t_b_c[i]))-1):
            f = key.index(t_b_c[i][j])
            state_count[f] += 1
            t = key.index(t_b_c[i][j+1])
            matrix[f][t] += 1
        
    for row in range(len(key)):
        for column in range(len(key)):
            if(state_count[row] != 0):
                matrix[row][column] /= state_count[row]
                matrix[row][column] = round(matrix[row][column],2)
    # print(matrix)
    return matrix
            


def item_candidates(item,int):
    m = create_Transition_Matrix()
    master_list = []
    n = 0
    for n in range(1,int+1):
        m = matrix_power(m, n)
        avg_prob = 0
        for row in range(len(m)):
            for column in range(len(m)):
                avg_prob += m[row][column]
        avg_prob = avg_prob/pow((len(m)),2)

        key_index = key.index(item)
        list = []
        for i in range(len(m)):
            item_and_prob = [key[i],round(m[key_index][i],3)]
            if item_and_prob[1] > avg_prob:
                list.append(item_and_prob)
        master_list.append(list)
    return(master_list)




