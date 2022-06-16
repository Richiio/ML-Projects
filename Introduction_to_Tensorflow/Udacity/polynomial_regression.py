import imp
from re import X
import numpy as np
import pandas as pd 
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

#Assign the data to predictor and outcome variables 
#Load the data
train_data = pd.read_csv("./data.csv")
X = train_data["VAR_X"].values.reshape(-1, 1)
Y = train_data["VAR_Y"].values

#Create a polynomial features
#Create a Polynomial Features Object, then fit and transform the predictor feature
poly_feat = PolynomialFeatures(degree=4)
X_poly = poly_feat.fit_transform(X)

#Make and fit the polynomial regression model
#Create a LinearRegression object and fit it to the polynomial predictor features
poly_model = LinearRegression(fit_intercept= False).fit(X_poly, Y)