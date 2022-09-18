# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 19:04:14 2022

@author: Hp
"""

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
data=pd.read_csv("CatData.csv")
data.head()
dfata=data.dropna()
print(data)

num=int(len(data)*0.8)
train =data[:num]
test=data[num:]

reg = linear_model.LinearRegression()
train_x = np.array(train[["Tail Length (cm)"]])
train_y = np.array(train[["Mass (kg)"]])
reg.fit(train_x,train_y)
coeff = reg.coef_
inter = reg.intercept_
print("Slope: ", coeff)
print("Intercept: ",inter)

plt.xlabel("Tail Length (cm)")
plt.ylabel("Mass (kg)")
plt.title("Tail Length vs Mass")
plt.scatter(train["Tail Length (cm)"],train["Mass (kg)"])
plt.plot(train_x,train_x*coeff[0]+inter, color = 'Red')
plt.show()