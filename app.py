import streamlit as st
import pandas as pd

st.title("💰 My First Budget App")

if 'my_list' not in st.session_state:
    st.session_state.my_list = []

item = st.text_input("What did you buy?")
cost = st.number_input("How much did it cost (₹)?", min_value=0)

if st.button("Save Entry"):
    if item and cost > 0:
        st.session_state.my_list.append({"Item": item, "Cost": cost})
        st.success("Saved successfully!")

if st.session_state.my_list:
    df = pd.DataFrame(st.session_state.my_list)
    st.write("### Total Spent: ₹", df["Cost"].sum())
    st.dataframe(df, use_container_width=True)
