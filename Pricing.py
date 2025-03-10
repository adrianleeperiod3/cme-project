from RandomHistory import create_random_transactions
from CorrellationScores import best_candidates
import random
import csv
from test import date

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
    prices = []
    for item, score in b:
        temp_addition = []
        mean_price = 0
        max_price = 0
        occurances = 0
        for i in range(len(data)):
            if data[i][3] == item:
                occurances += 1 
                mean_price += float(data[i][6])
                if float(data[i][6]) > max_price:
                    max_price = float(data[i][6])
        mean_price = mean_price / occurances
        t = round((mean_price + random.randrange(0,1)*(max_price-mean_price)),2)
        temp_addition.append(item)
        temp_addition.append(score)
        temp_addition.append(t)
        prices.append(temp_addition)
    return prices

def get_amounts(list,budget):
    corr_sum = 0
    item_and_pricing = []
    for i in range(len(list)):
      item_and_pricing.append([list[i][0]])
      corr_sum += list[i][1]
    for i in range(len(item_and_pricing)):
        print(int(((list[i][1]/corr_sum)*budget/list[i][2])+.5))
        item_and_pricing[i].append(int(((list[i][1]/corr_sum)*budget/list[i][2])+.5))

    return (item_and_pricing)
    
print(get_amounts(generate_prices(best_candidates(create_random_transactions(3),3,date)),500))
