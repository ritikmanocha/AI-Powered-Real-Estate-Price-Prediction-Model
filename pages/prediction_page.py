import streamlit as st
import numpy as np
from sklearn.linear_model import LinearRegression

# ---------- PAYMENT CHECK ----------
if not st.session_state.get("paid", False):
    st.warning("⚠️ Please complete payment first to access prediction 💳")
    st.stop()

# ---------- UI ----------
st.title("🏠 House Price Prediction")

area = st.number_input("Area (sqft)")
bed = st.number_input("Bedrooms")
bath = st.number_input("Bathrooms")
age = st.number_input("Age")

# ---------- MODEL ----------
model = LinearRegression()

X = np.array([
    [1000,2,1,10],
    [1500,3,2,8],
    [2000,3,2,6],
    [2500,4,3,5],
    [3000,4,3,4]
])

y = np.array([200000,300000,400000,500000,600000])

model.fit(X, y)

# ---------- PREDICTION ----------
if st.button("Predict Price"):
    pred = model.predict([[area, bed, bath, age]])
    st.success(f"Estimated Price: ${int(pred[0])}")
