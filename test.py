import streamlit as st
from RandomHistory import create_random_transactions
from CorrellationScores import best_candidates
from CorrellationScores import best_candidates_risky
import numpy as np
from RandomHistory import today
from Pricing import get_amounts
import pandas as pd
from Seasonality import freq_list
import altair as alt

st.title("Simulated Bundling Software")

st.sidebar.title("User Preferences")
history_length = st.sidebar.number_input("Number of Simulated Transactions", min_value=1, step=1)
budget = st.sidebar.number_input("Spending Budget", min_value=1000.0,step = 0.01)
risk_level = st.sidebar.selectbox("Trading Risk Level",['Safe','Risky','View Both'])

date = (f"{today.year}-{str(today.month).zfill(2)}-{str(today.day).zfill(2)}")

def safe_bundle(l):
    contract_names = []
    categories = []
    quantities = []
    prices = []
    p_cost = []
    total_cost = 0
    for i in range(len(l)):
        contract_names.append(l[i][0])
        quantities.append(l[i][2])
        prices.append(f"{l[i][3]:.2f}")
        categories.append(l[i][1])
        
        p_cost.append(f'{(l[i][2]*l[i][3]):.2f}')
    for item,cat,quantity,price in l:
         total_cost += quantity*price
    bundle_df = {'Contract':contract_names, 
                 'Category': categories,
                 'Quantity':quantities,
                 'Contract Price ($)':prices,
                 'Partial Cost($)': p_cost}
    st.header("Safe Bundle")
    st.subheader(f"Total Cost: ${total_cost:.2f}")
    st.dataframe(bundle_df)

    spread = []
    datums = []
    col = ['month']
    c = []
    months = [1,2,3,4,5,6,7,8,9,10,11,12]
    for item,cat,quantity,price in l:
        spread.append(freq_list(item))
        col.append(item)
        c.append(item)
    for i in range(len(months)):
        s = []
        s.append(months[i])
        for j in range(len(spread)):
            s.append(spread[j][i])
        datums.append(s)
    df = pd.DataFrame(datums, columns=col)
    st.subheader("Bundled Item Purchases Throughout the Year")
    st.bar_chart(df, x = 'month', y = c, stack= False, x_label="Month of the Year", y_label="Contracts Purchased")

def risky_bundle(l):
    contract_names = []
    categories = []
    quantities = []
    prices = []
    p_cost = []
    total_cost = 0
    for i in range(len(l)):
        contract_names.append(l[i][0])
        quantities.append(l[i][2])
        prices.append(f"{l[i][3]:.2f}")
        categories.append(l[i][1])
        
        p_cost.append(f'{(l[i][2]*l[i][3]):.2f}')
    for item,cat,quantity,price in l:
         total_cost += quantity*price
    bundle_df = {'Contract':contract_names,
                 'Category': categories,
                 'Quantity':quantities,
                 'Contract Price ($)':prices,
                 'Partial Cost($)': p_cost}
    st.header("Risky Bundle")
    st.subheader(f"Total Cost: ${total_cost:.2f}")
    st.dataframe(bundle_df)

    spread = []
    datums = []
    col = ['month']
    c = []
    months = [1,2,3,4,5,6,7,8,9,10,11,12]
    for item,cat,quantity,price in l:
        spread.append(freq_list(item))
        col.append(item)
        c.append(item)
    for i in range(len(months)):
        s = []
        s.append(months[i])
        for j in range(len(spread)):
            s.append(spread[j][i])
        datums.append(s)
    df = pd.DataFrame(datums, columns=col)
    st.subheader("Bundled Item Purchases Throughout the Year")
    st.bar_chart(df, x = 'month', y = c, stack= False, x_label="Month of the Year", y_label="Contracts Purchased")
    
st.divider() 

if st.sidebar.button("Apply Preferences"):
    h = create_random_transactions(history_length)
    
    if risk_level == 'Safe':
        amounts = get_amounts(best_candidates(h,5,date),.75*budget)
        if amounts == []:
            st.write("Budget too low to generate safe bundle. Please hit 'Apply Preferences' again.")
        else:
            safe_bundle(amounts)
    elif risk_level == 'Risky':
        amounts = get_amounts(best_candidates_risky(h,5,date),budget)
        if amounts == []:
            st.write("Budget too low to generate risky bundle. Please hit 'Apply Preferences' again.")
        else:
            risky_bundle(amounts)
    else:
        amounts_safe = get_amounts(best_candidates(h,5,date),.75*budget)
        amounts_risky= get_amounts(best_candidates_risky(h,5,date),budget)
        if amounts_safe == []:
          st.write("Budget too low to generate safe bundle. Please hit 'Apply Preferences' again.")
        else:
            safe_bundle(amounts_safe)
        st.divider()
        if amounts_risky == []:
            st.write("Budget too low to generate risky bundle. Please hit 'Apply Preferences' again.")
        else:
            risky_bundle(amounts_risky)
    st.divider()

    history = {
        'Transaction Number': [],
        'Contract Category': [],
        'Contract': [],
        'Price': [],
        'Quantity': [],
        'Overall Price': []
    }

    for i in range(len(h)):
        history['Transaction Number'].append(i+1)
        history['Contract Category'].append(h[i][2])
        history['Contract'].append(h[i][3])
        history['Price'].append(f'{h[i][6]:.2f}')
        history['Quantity'].append(h[i][5])
        history['Overall Price'].append(f'{h[i][7]:.2f}')
    
    hist = pd.DataFrame(history)
    st.header("Simulated Purchase History")
    st.dataframe(hist, hide_index=True)
    
        