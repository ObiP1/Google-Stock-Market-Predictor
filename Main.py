import math
import pandas as pd
import numpy as np
import pandas_datareader as web
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

#Retrieves data from Yahoo finance for respective dates and stock
df = web.DataReader('GOOG', data_source = 'yahoo', start='2015-01-01', end='2020-04-10')

#Creates plot to analyze previous closing values
plt.figure(figsize=(16,8))
plt.title('Previous Closing Prices')
plt.plot(df['Close'])
plt.xlabel('Year',fontsize=20)
plt.ylabel('Price of Stock in USD', fontsize=20)

#creation of new data fram with only close column
newData = df.filter(['Close'])
#Conversion of new data to numpy array
newDataset = newData.values
#Obtaining # of rows to train model on (80% of our data will be trained)
length_training_data = math.ceil(len(newDataset) * .8)

#Scaling of data
scale = MinMaxScaler(feature_range=(0,1))
scaled_data = scale.fit_transform(newDataset)

#Creation of training & scaled dataset
train_data = scaled_data[0:length_training_data, :]
#Splitting of data to x_train and y_train sets
x_train = []
y_train = []
# Allows us to utilize the previous 60 closing values and add them to respective arrays
for i in range(60, len(train_data)):
    x_train.append(train_data[i-60:i, 0])
    y_train.append(train_data[i,0])
    
#conversion of x_train and y_train to numpy arrays
x_train, y_train = np.array(x_train), np.array(y_train)
