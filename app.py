
import streamlit as st

st.title("Tip Calculator")

Cost = st.number_input("How much was your meal?", min_value=0.0, step=0.01)

Percent = st.number_input("What percent do you want to leave?", min_value=0, max_value=100, value=15)

if st.button("Calculate Tip"):
    Tip = Cost * (Percent / 100)
    Total = Cost + Tip

    st.write(f"Tip amount: ${Tip:.2f}")
    st.success(f"Total with tip: ${Total:.2f}")
