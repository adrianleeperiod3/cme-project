import csv
import bisect 
import numpy as np
from numpy.linalg import matrix_power 

with open("data.csv") as f:
    data=[tuple(line) for line in csv.reader(f)]

ordered_transactions = [] #orders objects with respect to transaction number
t_b_c = [] #orders purchased-item objects by individual users

key = []
for cust,trans,item, in data:
    count = 0
    for i in range (len(key)):
        if key[i] == item:
            count += 1
    if count == 0:
         key.append(item)
print(f"Key: \n{key}")

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

def order_by_transaction(): #orders transaction objects by sequential transaction IDs
    tempList = []
    for i in range (len(data)):
        bisect.insort(tempList, data[i][1])
    for t in tempList:
        for i in range(len(data)):
            if data[i][1] == t:
                tempObject = [extract_int(data[i][0]),extract_int(data[i][1]),data[i][2]]
                ordered_transactions.append(tempObject)
        
def transactions_by_customer(): #creates an array to order each individuals sequential transactions
    cust_blacklist = []
    for i in range (len(ordered_transactions)):
        temp_cust = ordered_transactions[i][0]
        if occurances(temp_cust) == 1:
            t_b_c.append([ordered_transactions[i][2]])
        else:
            tempItems = []
            for j in range (len(ordered_transactions)):
                if ordered_transactions[j][0] == temp_cust and temp_cust not in cust_blacklist:
                    tempItems.append(ordered_transactions[j][2])
            if len(tempItems) != 0:
                t_b_c.append(tempItems)
                cust_blacklist.append(temp_cust)
            
def create_Transition_Martix(): #creates the Markov Matrix
    order_by_transaction()
    transactions_by_customer()
    
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
    return matrix
            


def item_candidates(item,int):
    m = create_Transition_Martix()
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

   
    
item = "Soybeans"
print(f"List of Item Candidates Given {item}: \n{item_candidates(item,3)}")




