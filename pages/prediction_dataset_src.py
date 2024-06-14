import streamlit as st


st.header('Prediction using Data Sets Source Code')
st.subheader('This python code is implemented for Streamlit')
st.code(''' 
        
import streamlit as st
import pandas as pd
import pickle

# Load the trained model
filename = 'income_model.sav'
loaded_model = pickle.load(open(filename, 'rb'))

@st.cache_data
def predict_expenditure(features):
    return loaded_model.predict([features])

st.title("Filipino Family Income and Expenditure Predictor :smile:")
st.subheader("Enter family details to predict Total Food Expenditure:")

# Input fields
income = st.number_input("Total Household Income:", min_value=0)
family_size = st.slider("Total Number of Family members:", 1, 20)
household_head_age = st.number_input("Household Head Age:", min_value=0)
household_head_sex = st.selectbox("Household Head Sex:", ["Male", "Female"])

# Mapping sex to numerical values for model prediction
household_head_sex_num = 1 if household_head_sex == "Male" else 0

if st.button('Predict'):
    features = [income, family_size, household_head_age, household_head_sex_num]
    expenditure = predict_expenditure(features)
    st.write(f"Predicted Total Food Expenditure: {expenditure[0]:.2f}")
        
        ''')