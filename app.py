import streamlit as st
import pandas as pd
import pickle

model = pickle.load(open("model.pkl", "rb"))
df = pd.read_csv("Bengaluru_House_Data_Expanded.csv")

st.set_page_config(page_title="Real Estate AI", page_icon="🏡")
st.title("Bengaluru House Price Predictor + Risk Score")
st.dataframe(df)

sqft = st.number_input("Total Area (in sqft)", 300, 10000, 1000)
bath = st.selectbox("Bathrooms", [1, 2, 3, 4, 5])
bhk = st.selectbox("BHK", [1, 2, 3, 4, 5])

if st.button("Predict Price"):
    input_df = pd.DataFrame([[sqft, bath, bhk]], columns=["total_sqft", "bath", "BHK"])
    price = model.predict(input_df)[0]

    score = 0
    if sqft < 1000: score += 1
    if bath < bhk: score += 1
    risk = "High" if score == 2 else "Medium" if score == 1 else "Low"

    st.success(f"Estimated Price: ₹{round(price, 2)} Lakhs")
    st.warning(f"Risk Score: {risk}")