import csv
import bisect 

with open("data_copy.csv") as f:
    data=[tuple(line) for line in csv.reader(f)]

ordered_transactions = []

def order_by_transaction():
    tempList = []
    for i in range (len(data)):
        bisect.insort(tempList, data[i][1])
    for t in tempList:
        for i in range(len(data)):
            if data[i][1] == t:
                ordered_transactions.append(data[i])
        

order_by_transaction()
print(ordered_transactions)


