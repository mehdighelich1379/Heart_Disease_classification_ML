import streamlit as st
import pickle
import pandas as pd

import streamlit as st

st.image('https://www.darmankade.com/blog/wp-content/uploads/2019/12/Is-Thyroid-Dangerous10.jpg', use_column_width=True)


with open('catboost_model.txt', 'rb') as model_file:
    model = pickle.load(model_file)
st.sidebar.header("Enter the details for prediction:🔍")

age = st.sidebar.number_input("Enter your age", min_value=0, max_value=100, value=0)
sex = st.sidebar.number_input("Enter your sex", min_value=0, max_value=1, value=0)
cp = st.sidebar.number_input("Enter your cp", min_value=0, max_value=3, value=0)
trestbps = st.sidebar.number_input("Enter your trestbps", min_value=0, max_value=300, value=0)
chol = st.sidebar.number_input("Enter your chol", min_value=0, max_value=500, value=0)
restecg = st.sidebar.number_input("Enter your restecg", min_value=0, max_value=2, value=0)
thalach = st.sidebar.number_input("Enter your thalach", min_value=0, max_value=200, value=0)
exang = st.sidebar.number_input("Enter your exang", min_value=0, max_value=1, value=0)
oldpeak = st.sidebar.number_input("Enter your oldpeak", min_value=0, max_value=5, value=0)
slope = st.sidebar.number_input("Enter your slope", min_value=0, max_value=2, value=0)
ca = st.sidebar.number_input("Enter your ca", min_value=0, max_value=4, value=0)
thal = st.sidebar.number_input("Enter your thal", min_value=0, max_value=3, value=0)


user_input = pd.DataFrame({
    'age': [age],
    'sex': [sex],
    'cp': [cp],
    'trestbps': [trestbps],
    'chol': [chol],
    'restecg': [restecg],
    'thalach': [thalach],
    'exang': [exang],
    'oldpeak': [oldpeak],
    'slope': [slope],
    'ca': [ca],
    'thal': [thal]
})

prob = model.predict_proba(user_input)[0][1]

st.sidebar.write(f"Probability of Heart Disease: {prob:.2f}")

if st.button("Predict"):
    if prob >= 0.6:
        st.error("The patient has a high probability of having heart disease.")
    else:
        st.success("The patient has a low probability of having heart disease.")
