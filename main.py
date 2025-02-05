import csv
with open("data.csv") as f:
    data=[tuple(line) for line in csv.reader(f)]

def extract_int(str):
    return int(str[3:],10)

ordered_transactions = []

def order_by_transaction():
    for i in range (len(data)):
        if (len(ordered_transactions)) == 0:
            ordered_transactions.append(data[i])
        # else:
        #     for j in range (len(ordered_transactions)):
        #         if (extract_int(data[i][1])) < (extract_int(ordered_transactions[j][1])):
        #             ordered_transactions.insert(j,data[i])

order_by_transaction()
print()


