import csv
import bisect 

with open("data_copy.csv") as f:
    data=[tuple(line) for line in csv.reader(f)]

ordered_transactions = []
t_b_c = []

def extract_int(str):
    r = []
    for i in str:
        if i.isdigit():
            r.append(i)
    return int(''.join(r))

def occurances(int):
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
        
def transactions_by_customer():
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
            
        


order_by_transaction()
print(ordered_transactions)
transactions_by_customer()
print(t_b_c)


