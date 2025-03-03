import streamlit as st

st.title("Bundling Software")

user_id = st.text_input("Number of Past Transactions")
budget = st.number_input("Budget", min_value=0.0, step=0.01)
risk = st.radio("risk",["Safe","Risky"])

if st.button("Submit"):
    for i in range(int(budget)):
        st.write(f"Budget = {budget} '\n'")