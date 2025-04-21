import streamlit as st
import pickle
import pandas as pd

import streamlit as st

st.image('https://www.darmankade.com/blog/wp-content/uploads/2019/12/Is-Thyroid-Dangerous10.jpg' , use_container_width=True)


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
oldpeak = st.sidebar.number_input("Enter your oldpeak", min_value=0.0, max_value=10.0, value=0.1)
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
prob = 1 - prob

st.sidebar.write(f"Probability of Heart Disease: {prob:.2f}")

if st.button("Predict"):
    if prob >= 0.6:
        st.error("The patient has a high probability of having heart disease.")
    else:
        st.success("The patient has a low probability of having heart disease.")

st.markdown("### Doctor AI Analysis")

analysis = ""

# Cholesterol
if chol > 240:
    analysis += "- High cholesterol level detected. Consider dietary and lifestyle adjustments.\n"
else:
    analysis += "- Cholesterol level is within a normal range.\n"

# Resting Blood Pressure
if trestbps > 140:
    analysis += "- Elevated resting blood pressure. Monitor regularly and consult a physician.\n"
else:
    analysis += "- Resting blood pressure appears to be normal.\n"

# Exercise Induced Angina
if exang == 1:
    analysis += "- Exercise-induced angina reported. This may indicate underlying heart issues.\n"
else:
    analysis += "- No signs of angina during exercise — a positive sign.\n"

# Maximum Heart Rate Achieved
if thalach < 100:
    analysis += "- Low maximum heart rate. This could suggest a limitation in cardiac output.\n"
elif thalach > 140:
    analysis += "- Good heart rate response during physical activity.\n"
else:
    analysis += "- Heart rate is moderate. Further assessment may be needed based on other indicators.\n"

# Oldpeak (ST depression)
if oldpeak > 2:
    analysis += "- Significant ST depression observed, which may reflect ischemic changes.\n"
else:
    analysis += "- ST depression is within a safe range.\n"

st.info(analysis)
