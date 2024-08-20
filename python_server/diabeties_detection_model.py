# -*- coding: utf-8 -*-
"""Diabeties Detection Model

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1lRbDZ0znTvRhNb8ySRFrkCI9QS12Eum_
"""

# import joblib
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler

"""# Data collection and analysis"""

Dataset=pd.read_csv('D:\diabetes.csv')

Dataset.head() # gives first five
Dataset.shape # here 768 rows and 9 columns
Dataset.describe() # gives statistical measures of the data

# pd.read_csv?

Dataset['Outcome'].value_counts() # here 500 are 0 and 268 diabetic patients
X=Dataset.drop(columns='Outcome',axis=1) # drop last column  here axis =1  used when droping a column and axis=0 used when droping a row
Y=Dataset['Outcome'] # gives the values of the columns Outcome to y

Dataset.groupby('Outcome').mean() # Here it would calculate the mean of the Diabetic and non diabetic patients
#since outcome columns have only two values

print(X)
print(Y)

scaler=StandardScaler()
scaler.fit(X)
Standardized_X=scaler.transform(X)
print(Standardized_X)
Y=Dataset['Outcome'] # gives the values of the columns Outcome to y

"""Train Test Split"""

X_train,X_test,Y_train,Y_test=train_test_split(Standardized_X,Y,test_size=0.1,stratify=Y,random_state=2)
 # stratify is done to y since we want y to be equally distibuted means the ratio of o and 1 would be same in both almost
# print(X_train )

print(Y.value_counts())
print(Y_train.value_counts())
print(Y_test.value_counts())

classifier=svm.SVC(kernel='linear')
# training the model
classifier.fit(X_train,Y_train)
# prediction the value
X_train_prediction =classifier.predict(X_train)
print(accuracy_score(Y_train,X_train_prediction) )

X_test_prediction=classifier.predict(X_test)

print(accuracy_score(Y_test,X_test_prediction))

input_data=(8,99,84,0,0,35.4,0.388,50)
# here we have to change it in numpy array since it is more efficient and faster
input_data_numpy=np.asarray(input_data)
input_data_numpy.shape # here shape is like 1D array
input_data_reshaped=input_data_numpy.reshape(1,-1)
input_data_reshaped.shape # here shape is like 2D array and is row vector with 8 columns

input_data_standardized=scaler.transform(input_data_reshaped)
print(input_data_standardized)

prediction=classifier.predict(input_data_standardized)
print(prediction)

if(prediction[0]==0):
  print('The person is not diabetic')
else:
  print('The person is diabetic')

