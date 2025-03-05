from test import bundle
import random
import csv

with open("datafull.csv") as f:
    data=[line for line in csv.reader(f)]

def avg_purchase(history):
    avg = 0
    count = 0
    for cust,trans,type,item,date,quantity,price,value in history:
        avg += value
        count += 1
    avg = avg / count
    return round(avg,2)

def generate_prices(b):
    prices = [0]*len(b)
    for item, score in b:
        temp_addition = []
        mean_price = 0
        max_price = 0
        occurances = 0
        for i in range(len(data)):
            if data[i][3] == item:
                occurances += 1 
                mean_price += data[i][6]
                if data[i][6] > max_price:
                    max_price = data[i][6]
        mean_price = mean_price / occurances
        temp_addition.append(item)
        temp_addition.append(mean_price + random.randrange(0,1)*(max_price-mean_price))
    return prices


        
