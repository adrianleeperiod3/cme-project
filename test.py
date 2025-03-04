import streamlit as st
from RandomHistory import create_random_transactions

st.title("Bundling Software")

budget = st.number_input("History Length", min_value=0, step=1)
risk = st.radio("Preferred Risk Level",["Safe","Risky"])

h = create_random_transactions(budget)
if st.button("Submit"):
    for i in range(int(budget)):
        st.write(f"Purchase {i+1}: {h[i][2]} on {h[i][4]} \n")