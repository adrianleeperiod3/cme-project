import streamlit as st
from RandomHistory import create_random_transactions
from CorrellationScores import best_candidates
import numpy as np
from RandomHistory import today

st.title("Bundling Software")

st.sidebar.title("User Preferences")
history_length = st.sidebar.number_input("Number of Simulated Transactions:", min_value=0, step=1)
risk_level = st.sidebar.selectbox("Trading Risk Level: ",['Safe','Risky','View Both'])


h = create_random_transactions(history_length)
bundle = best_candidates(h,3,today)
if st.sidebar.button("Apply Preferences"):
    for i in range(len(bundle)):
        st.write(f"Purchase {i+1}: {bundle[i][0]} \n")