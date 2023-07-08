# -*- coding: utf-8 -*-
"""DL PR 3 deep neural network for performing classification task..ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1txCW2bjMFobXuZ3A4KVE0ceV1-fGTEsS
"""


from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense
import numpy as np

dataset = loadtxt('pima-indians-diabetes.csv',delimiter=',')

dataset

x = dataset[:,0:8]
y = dataset[:,8]

x

y

model = Sequential()
model.add(Dense(12,input_dim=8,activation='relu'))
model.add(Dense(8,activation='relu'))
model.add(Dense(1,activation='sigmoid'))

model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])
model.fit(x,y,epochs=150,batch_size=10)

_,accuracy=model.evaluate(x,y)

print("Accuracy of model is",(accuracy*100))

prediction =model.predict(x)

exec("for i in range(5):print(x[i].tolist(),prediction[i],y[i])")