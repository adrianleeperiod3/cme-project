import streamlit as st
from RandomHistory import create_random_transactions
from CorrellationScores import best_candidates
import numpy as np
from RandomHistory import today
from Pricing import get_amounts

st.title("Bundling Software")

st.sidebar.title("User Preferences")
history_length = st.sidebar.number_input("Number of Simulated Transactions:", min_value=1, step=1)
budget = st.sidebar.number_input("Spending Budget:", min_value=0.01,step = 0.01)
risk_level = st.sidebar.selectbox("Trading Risk Level: ",['Safe','Risky','View Both'])

date = (f"{today.year}-{str(today.month).zfill(2)}-{str(today.day).zfill(2)}")

if st.sidebar.button("Apply Preferences"):
    h = create_random_transactions(history_length)
    bundle = best_candidates(h,3,date)
    amounts = get_amounts(bundle,budget)
    if amounts == "Budget Too Low To Support Bundle Purchases":
            st.write(amounts)
    else:
        for i in range(len(amounts)): 
            st.write(f"Purchase {i+1}: {amounts[i][1]} contracts of {amounts[i][0]} \n")