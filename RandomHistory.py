from TransitionMatrix import key
from datetime import datetime
import pytz
import random
import csv

with open("datafull.csv") as f:
    data=[line for line in csv.reader(f)]

today = datetime.now(pytz.timezone('America/Chicago'))

def create_random_transactions(amount):
    transactions = []
    futures = ["Natural_Gas","Corn","Crude_Oil","S&P500_Call","Gold","S&P500"]
    options = ["Gold_Put","Oil_Call","Treasury_Put"]
    agriculture = ["Live_Cattle","Wheat","Soybeans","Lean_Hogs"]
    thirty_one_days = [1,3,5,7,8,10,12]
    thirty_days = [4,6,9,11]
    for i in range(amount):
        temp_trans = []
        temp_trans.append("CUSTUSER")
        temp_trans.append(f"TXN{str(i+1).zfill(3)}")
        temp_item = key[random.randrange(12)]
        if temp_item in futures:
              temp_trans.append("Futures")
        elif temp_item in options:
              temp_trans.append("Options")
        else:
              temp_trans.append("Agriculture")
        temp_trans.append(temp_item)
        year = 2000 + random.randrange(today.year-2000)
        if year == today.year:
              month = random.randrange(1,today.month+1)
        else:
              month = random.randrange(1,12)
        if month == today.month:
              day = random.randrange(1,today.day+1)
        else:
                if month in thirty_one_days:
                    day = random.randrange(1,32)
                elif month in thirty_days:
                    day = random.randrange(1,31)
                else:
                    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
                          day = random.randrange(1,30)
                    else:
                          day = random.randrange(1,29)
        temp_trans.append(f"{year}-{str(month).zfill(2)}-{str(day).zfill(2)}")
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
        rand_quantity = random.randrange(1,max_quantity)
        rand_price = round(random.randrange(1)*(max_price-mean_price) + mean_price,2)
        temp_trans.append(rand_quantity)
        temp_trans.append(rand_price)
        temp_trans.append(round(rand_quantity*rand_price,2))
        transactions.append(temp_trans)
    return transactions



    
