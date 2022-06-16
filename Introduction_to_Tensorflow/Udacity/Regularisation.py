from email import header
import numpy as np
import pandas as pd
from sklearn.linear_model import Lasso

#Assign the data to predictor and outcome variables
#Load the data
train_data = pd.read_csv("data1.csv", header = None )
X = train_data.iloc[:,:-1]
y = train_data.iloc[:, -1]

#Create the linear regression model with lasso regularization
lasso_reg = Lasso()

#Fit the model
lasso_reg.fit(X, y)

#Retrieve and print out hte coefficients from the regression model
reg_coef = lasso_reg.coef_
print(reg_coef)