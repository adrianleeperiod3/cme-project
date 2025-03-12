import streamlit as st
from RandomHistory import create_random_transactions
from CorrellationScores import best_candidates
from CorrellationScores import best_candidates_risky
import numpy as np
from RandomHistory import today
from Pricing import get_amounts
import pandas as pd

st.title("Bundling Software")

st.sidebar.title("User Preferences")
history_length = st.sidebar.number_input("Number of Simulated Transactions", min_value=1, step=1)
budget = st.sidebar.number_input("Spending Budget", min_value=0.01,step = 0.01)
risk_level = st.sidebar.selectbox("Trading Risk Level",['Safe','Risky','View Both'])

date = (f"{today.year}-{str(today.month).zfill(2)}-{str(today.day).zfill(2)}")

def safe_bundle(l):
    contract_names = []
    quantities = []
    prices = []
    p_cost = []
    total_cost = 0
    for i in range(len(l)):
        contract_names.append(l[i][0])
        quantities.append(l[i][1])
        prices.append(f"{l[i][2]:.2f}")
        
        p_cost.append(f'{(l[i][2]*l[i][1]):.2f}')
    for item,quantity,price in l:
         total_cost += quantity*price
    bundle_df = {'Contract':contract_names, 
                 'Quantity':quantities,
                 'Contract Price ($)':prices,
                 'Partial Cost($)': p_cost}
    st.subheader(f"Safe Bundle || Total Cost:${total_cost:.2f}")
    st.dataframe(bundle_df)

def risky_bundle(l):
    contract_names = []
    quantities = []
    prices = []
    p_cost = []
    total_cost = 0
    for i in range(len(l)):
        contract_names.append(l[i][0])
        quantities.append(l[i][1])
        prices.append(f"{l[i][2]:.2f}")
        
        p_cost.append(f'{(l[i][2]*l[i][1]):.2f}')
    for item,quantity,price in l:
         total_cost += quantity*price
    bundle_df = {'Contract':contract_names, 
                 'Quantity':quantities,
                 'Contract Price ($)':prices,
                 'Partial Cost($)': p_cost}
    st.subheader(f"Risky Bundle || Total Cost:${total_cost:.2f}")
    st.dataframe(bundle_df)
     
if st.sidebar.button("Apply Preferences"):
    h = create_random_transactions(history_length)
    
    if risk_level == 'Safe':
        amounts = get_amounts(best_candidates(h,5,date),budget)
        if amounts == []:
            st.write("Budget is too low to support safe bundle purchases.")
        else:
            print(amounts)
            safe_bundle(amounts)
    elif risk_level == 'Risky':
        amounts = get_amounts(best_candidates_risky(h,5,date),budget)
        if amounts == []:
            st.write("Budget is too low to support risky bundle purchases.")
        else:
            print(amounts)
            risky_bundle(amounts)
    else:
        amounts_safe = get_amounts(best_candidates(h,5,date),budget)
        amounts_risky= get_amounts(best_candidates_risky(h,5,date),budget)
        if amounts_safe == []:
            st.write("Budget is too low to support safe bundle purchases.")
        else:
            print(amounts_safe)
            safe_bundle(amounts_safe)
        if amounts_risky == []:
            st.write("Budget is too low to support risky bundle purchases.")
        else:
            print(amounts_risky)
            risky_bundle(amounts_risky)
        