
def avg_purchase(history):
    avg = 0
    count = 0
    for cust,trans,type,item,date,quantity,price,value in history:
        avg += value
        count += 1
    avg = avg / count
    return round(avg,2)