import streamlit as st
import pickle
import pandas as pd



with open('Final_Heart_Model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)
st.write("Enter the details for prediction:")

age = st.number_input('Age', min_value=1, max_value=120, value=60)
sex = st.selectbox('Sex', options=[0, 1], format_func=lambda x: 'Male' if x == 1 else 'Female')
cp = st.selectbox('CP', options=[0, 1, 2, 3])
trestbps = st.number_input('Resting Blood Pressure', min_value=0, max_value=300, value=120)
chol = st.number_input('Cholesterol', min_value=0, max_value=600, value=200)

restecg = st.selectbox('Resting Electrocardiographic Results', options=[0, 1, 2])
thalach = st.number_input('Maximum Heart Rate Achieved', min_value=0, max_value=250, value=150)
exang = st.selectbox('Exercise Induced Angina', options=[0, 1])
oldpeak = st.number_input('Oldpeak', value=0.0)
slope = st.selectbox('Slope of the Peak Exercise ST Segment', options=[0, 1, 2])
ca = st.selectbox('Number of Major Vessels Colored by Fluoroscopy', options=[0, 1, 2, 3])
thal = st.selectbox('Thalassemia', options=[0, 1, 2, 3])

# ایجاد دیتا فریم برای ورودی‌های جدید
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

# پیش‌بینی با استفاده از مدل
if 'model' in locals():
    prediction = model.predict(user_input)
    
    # نمایش نتیجه پیش‌بینی
    if prediction[0] == 1:
        st.write('Prediction: Heart Disease Detected')
    else:
        st.write('Prediction: No Heart Disease')