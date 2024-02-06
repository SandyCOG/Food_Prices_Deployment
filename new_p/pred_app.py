#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 10:36:39 2024

@author: rabiat
"""

import streamlit as st
#import pandas as pd
#import numpy as np

import pickle

html_temp = """
<div style="background-color:yellow;padding:1.5px">
<h1 style="color:black;text-align:center;">Agricultural food price prediction</h1>
</div><br>"""
st.markdown(html_temp, unsafe_allow_html=True)


st.write("\n\n"*2)

#filename = 'Prediction_page/xgb_pipeline.pkl'
#model = pickle.load(open(filename, 'rb'))



with open('xgb_pipeline.pkl', 'rb') as file:
    model = pickle.load(file)

def main():
    #st.title('Your Streamlit App with Pickled Model')
    with st.sidebar:
        st.subheader('Food Crops to Predict Price')
    # Input features for making predictions
     
        states = st.selectbox("Choose state:", ['Abia', 'Abuja', 'Adamawa', 'Akwa Ibom', 'Anambra', 'Bauchi',
       'Bayelsa', 'Benue', 'Borno', 'Cross River', 'Delta', 'Ebonyi',
       'Edo', 'Ekiti', 'Enugu', 'Gombe', 'Imo', 'Jigawa', 'Kaduna',
       'Kano', 'Katsina', 'Kebbi', 'Kogi', 'Kwara', 'Lagos', 'Niger',
       'Ogun', 'Ondo', 'Osun', 'Oyo', 'Plateau', 'Rivers', 'Sokoto',
       'Taraba', 'Yobe', 'Zamfara', 'Nassarawa'])
        Year = st.text_input("Enter year:", 2001)
        Annual_rainfall_mm = st.text_input("Enter annual rainfall:", "2344.19")
        Seasonal_length_days = st.text_input("Enter seasonal lenght:", "269.1")
        Latitude = st.text_input("Choose Latitude:", 5.45)
        Longitude = st.text_input("Choose Longitude:", 7.51)
        crops = st.selectbox("Choose crop:", ['Beans brown,sold loose', 'Rice Medium Grained',
       'Gari white,sold loose', 'Beans:white black eye. sold loose',
       'Gari yellow,sold loose', 'Onion bulb', 'Broken Rice (Ofada)',
       'Tomato', 'Plantain(unripe)', 'Maize grain white sold loose',
       'Yam tuber', 'Maize grain yellow sold loose', 'Plantain(ripe)'])
        Month = st.text_input("Choose Month:", 12)
        Annual_all_item_inflation = st.text_input("Enter Annual_all_item_inflation:", "16.5")
        Monthly_all_item_inflation = st.text_input("Enter Monthly_all_item_inflation:", "17.4")
        Annual_food_inflation = st.text_input("Enter Annual_food_inflation:", "20.9")
        Monthly_food_inflation  = st.text_input("Enter Monthly_food_inflation:", "22.3")
    # Make a prediction using the loaded model
    
    input_data= pd.DataFrame([[states, Year, Annual_rainfall_mm, Seasonal_length_days, Latitude,
                            Longitude, crops, Month, Annual_all_item_inflation, Monthly_all_item_inflation,
                            Annual_food_inflation, Monthly_food_inflation]], 
                             columns=["states", "Year", "Annual_rainfall_mm", "Seasonal_length_days", "Latitude",
                                                    "Longitude", "crops", "Month", "Annual_all_item_inflation", "Monthly_all_item_inflation",
                                                    "Annual_food_inflation", "Monthly_food_inflation"])
    
    prediction = model.predict(input_data)

    st.subheader('Prediction')
    st.write(f'The model predicts: {prediction[0]}')

if __name__ == '__main__':
    main()
