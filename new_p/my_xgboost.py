#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 09:29:10 2024

@author: rabiat
"""

import pandas as pd
#import numpy as np
#import datetime



# Sklearn tools
from sklearn.model_selection import train_test_split
#from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
#from sklearn.model_selection import cross_validate, KFold, GridSearchCV
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
#from sklearn.ensemble import RandomForestRegressor
from sklearn.compose import ColumnTransformer
from xgboost import XGBRegressor

import pickle

#Import the dataset
price_df = pd.read_csv("food_price_dataset.csv")


# split the features into numerical and categorical 
#num_cols = list(price_df.select_dtypes(exclude = 'object').columns)
num_cols =   ['Year', 'Annual_rainfall_mm', 'Seasonal_length_days', 'Latitude', 'Month', 'Annual_all_item_inflation', 'Monthly_all_item_inflation', 'Annual_food_inflation', 'Monthly_food_inflation']        # Remove the target variable
categorical_list= ['states','crops']
#print(num_cols)
target = ['Price/Kg(Naira)']


# Extract the features and target variable 
df3= price_df.copy()
X=df3[num_cols + categorical_list]
y= df3[target]


# Pipeline for numerical and categorical columns

num_pipe = Pipeline(steps=[("scale", MinMaxScaler())])
cat_pipe = Pipeline(steps=[("encoder", OneHotEncoder())])

#Performing transformation with the pipelines
column_transform = ColumnTransformer(transformers=[("num_trans", num_pipe, num_cols),
                                                  ("cat_trans", cat_pipe, categorical_list)],
                                     n_jobs=-1)



# xgboost pipeline
xgb_regressor = XGBRegressor(learning_rate=0.1,
    n_estimators= 150,
    max_depth= 15)

xgb_pipeline = Pipeline(steps= [("transformation", column_transform),
                           ("model", xgb_regressor)])


# Train test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 0.2, random_state=42)


# Train the model 
xgb_pipeline.fit(X_train, y_train)

# Make prediction
predicted = xgb_pipeline.predict(X_test)


with open('xgb_pipeline.pkl', 'wb') as file:
    pickle.dump(xgb_pipeline, file)
    
    
    
    
R2 = r2_score(y_test, predicted)
print(f"R2-score {R2}")


MSE = mean_squared_error(y_test, predicted)
print(f"Mean squared error: {MSE}")

MAE = mean_absolute_error(y_test, predicted)
print(f"Mean absolute error: {MAE}")