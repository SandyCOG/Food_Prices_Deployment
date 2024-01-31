# -*- coding: utf-8 -*-

import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

import sklearn
#import xgboost
#from xgboost import XGBRegressor
import pickle

html_temp = """
<div style="background-color:yellow;padding:1.5px">
<h1 style="color:black;text-align:center;">Used Car Price Prediction</h1>
</div><br>"""
st.markdown(html_temp, unsafe_allow_html=True)


st.write("\n\n"*2)

filename = 'Prediction_page/food-price-prediction-model.pkl'
model = pickle.load(open(filename, 'rb'))

with st.sidebar:
    st.subheader('Food Crops to Predict Price')

    Date = st.text_input("Enter a date:", "default_value")
    Crops = st.select_box("Choose crop:", df['crops'].unique())
    State = st.select_box("Choose state:", df['states'].unique())

# When the user clicks a button or interacts with an input element, make a prediction
 if st.button("Predict"):
     #predictions based on user input
     prediction = model.predict([[Date, Crops, State]])

    # Display the prediction
     st.write(f"Predicted Price: {prediction[0]}")
        
#my_dict = {"make_model":make_model, "hp_kW":hp_kW, "age":age, "km":km, "Gears":Gears, "Gearing_Type":Gearing_Type}
#df = pd.DataFrame.from_dict([my_dict])

#cols = {
   # "make_model": "Car Model",
   # "hp_kW": "Horse Power",
   # "age": "Age",
   # "km": "km Traveled",
   # "Gears": "Gears",
  #  "Gearing_Type": "Gearing Type"
#}

#df_show = df.copy()
#df_show.rename(columns = cols, inplace = True)
#st.write("Selected Specs: \n")
#st.table(df_show)


#if st.button("Predict"):
 #   pred = model.predict(df)
 #   col1, col2 = st.columns(2)
 #   col1.write("The estimated value of car price is €")
 #   col2.write(pred[0].astype(int))


#st.write("\n\n")
