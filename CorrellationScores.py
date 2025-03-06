from Seasonality import establish_monthly_patterns
from TransitionMatrix import item_candidates
from TransitionMatrix import key
from RandomHistory import create_random_transactions

def get_item_category(item):
    futures = ["Natural_Gas","Corn","Crude_Oil","S&P500_Call","Gold","S&P500"]
    options = ["Gold_Put","Oil_Call","Treasury_Put"]
    agriculture = ["Live_Cattle","Wheat","Soybeans","Lean_Hogs",]
    if item in futures:
        return 0
    elif item in options:
        return 1
    else:
        return 2

def is_month_max(item,month):
    patterns = establish_monthly_patterns()
    for i in range(len(patterns)):
        if item == patterns[i][0]:
            if month in patterns[i][1]:
                return True
            else:
                return False

def get_seasonality_score(list):
    patterns = establish_monthly_patterns()
    score = 0
    for trans in list:
        pattern_id = 0
        for i in range(len(patterns)):
            if trans[3] == patterns[i][0]:
                pattern_id = i
        if int(trans[4][5:7]) in patterns[pattern_id][1]:
            score +=1 
    if len(list) > 0:
        return(round(score/len(list),3))
    return 0

def get_grouping_scores(list):
    futures = ["Natural_Gas","Corn","Crude_Oil","S&P500_Call","Gold","S&P500"]
    options = ["Gold_Put","Oil_Call","Treasury_Put"]
    agriculture = ["Live_Cattle","Wheat","Soybeans","Lean_Hogs",]
    futures_score = 0
    options_score = 0
    agriculture_score = 0
    for trans in list:
        if trans[2] == "Futures":
            futures_score += 1
        elif trans[2] == "Options":
            options_score += 1
        else:
            agriculture_score += 1
    if len(list) > 0:
        futures_score = round(futures_score / len(list),3)
        options_score = round(options_score / len(list),3)
        agriculture_score = round(agriculture_score / len(list),3)
    return([futures_score,options_score,agriculture_score])

def best_candidates(list,future_steps,date):
    grouping_score = get_grouping_scores(list)
    seasonality_score = get_seasonality_score(list)
    current_month = int(date[5:7])
    patterns = establish_monthly_patterns()
    most_recent_purchase = list[len(list)-1]
    candidates = item_candidates(most_recent_purchase[3],future_steps)
    for step in candidates:
        for i in range(len(step)):
            if is_month_max(step[i][0],current_month):
                step[i][1] = round(step[i][1] + grouping_score[get_item_category(step[i][0])] + seasonality_score,8)
            else:
                step[i][1] = round(step[i][1] + grouping_score[get_item_category(step[i][0])],8)
    best_list = []
    for step in candidates:
        highest_score = 0
        highest_score_index = 0
        for i in range(len(step)):
            if step[i][1] > highest_score:
                highest_score = step[i][1]
                highest_score_index = i
        best_list.append(step[highest_score_index])
    return(best_list)
        





