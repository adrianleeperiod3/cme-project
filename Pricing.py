from RandomHistory import create_random_transactions
from CorrellationScores import best_candidates
import random
import csv
from RandomHistory import today

with open("datafull.csv") as f:
    data=[line for line in csv.reader(f)]

date = (f"{today.year}-{str(today.month).zfill(2)}-{str(today.day).zfill(2)}")

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

def trim(l):
    print(l)
    g = []
    for i in range(len(l)):
        if l[i][1] != 0:
            g.append(l[i])  
        for i in range(len(g)):
            for j in range(len(g)):
                if g[i][0] == g[j][0] and i != j:
                    g.pop(i)
    print(g)
    return(g)

def get_amounts(list,budget):
    corr_sum = 0
    item_and_pricing = []
    bundle_price = 0
    for i in range(len(list)):
      item_and_pricing.append([list[i][0]])
      corr_sum += list[i][1]
    for i in range(len(list)):
        temp_item = list[i][0]
        max_quantity = 0
        mean_price = 0
        max_price = 0
        occurances = 0
        for cust,trans,type,item,date,quantity,price,value in data:
            if item == temp_item:
                occurances += 1
                if int(quantity) > max_quantity:
                    max_quantity = int(quantity)
                mean_price += float(price)
                if float(price) > max_price:
                    max_price = float(price)
        mean_price = mean_price / occurances
        rand_price = round(random.randrange(1)*(max_price-mean_price) + mean_price,2)
        item_and_pricing[i].append(int(((list[i][1]/corr_sum)*budget/rand_price)+.5))
        bundle_price += rand_price*item_and_pricing[i][1]
    while(bundle_price > budget):
        if item_and_pricing[len(item_and_pricing)-1][1] == 0:
            return("Budget Too Low To Support Bundle Purchases")
        else:
            item_and_pricing[len(item_and_pricing)-1][1] -= 1
    f = trim(item_and_pricing)
    if f == []:
        return("Budget Too Low To Support Bundle Purchases")
    else:
        return(f)
    


