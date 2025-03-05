import streamlit as st
from RandomHistory import create_random_transactions

st.title("Bundling Software")

st.sidebar.title("User Preferences")
history_length = st.sidebar.number_input("Number of Simulated Transactions:", min_value=0, step=1)
risk_level = st.sidebar.selectbox("Trading Risk Level: ",['Safe','Risky','View Both'])


h = create_random_transactions(history_length)
if st.sidebar.button("Apply Preferences"):
    for i in range(int(history_length)):
        st.write(f"Purchase {i+1}: {h[i][2]} on {h[i][4]} \n")