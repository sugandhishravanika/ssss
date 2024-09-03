# -*- coding: utf-8 -*-
"""C.I.E=3

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Icxg8pDff8M1ucH0Sb4vTDtKXJpbi-xW
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer # Changed simpleImputer to SimpleImputer
from sklearn.datasets import fetch_california_housing # Fixed typo in function name
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error

data= fetch_california_housing()
data

df = pd.DataFrame(data.data, columns=data.feature_names)
df['PRICE'] = data.target
print(df)

df.describe()

df.shape

df.info()

X = df.drop('PRICE', axis=1)
y = df['PRICE']
X
y

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=4)
print(X_train)
print(y_train)

md=LinearRegression()
md.fit(X_train,y_train)

yprd=md.predict(X_test)
yprd

mse=mean_squared_error(y_test,yprd)
mse