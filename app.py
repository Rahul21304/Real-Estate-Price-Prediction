import streamlit as st
import numpy as np 
import joblib

scaler = joblib.load("scaler.pkl")

model = joblib.load("model.pkl")

st.title("Real Estate Price Prediction")

st.divider()

bed = st.number_input("Enter the number of Bedrooms", value = 0, step = 1)
bath = st.number_input("Enter the number of Bathrooms", value = 0, step = 1)
size = st.number_input("Enter the size in Sqft", value = 0, step = 500)

X = [bed,bath,size]
#  x = ['bed', 'bath', 'house_size']
st.divider()
 
predictbutton = st.button("Predict!")

st.divider()

if predictbutton:

    st.balloons()

    X1 = np.array(X)

    X_array = scaler.transform([X1])

    prediction = model.predict(X_array)[0]

    st.write(f"The predicted Price is {prediction:.1f}")

else:
   
   "please use the button for prediction"
