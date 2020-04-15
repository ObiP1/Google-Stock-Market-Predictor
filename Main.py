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

#Reshapes training data into 3 dimensions for usabilty
x_train =np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))

#Creation of Long Short Term Memory (LSTM) model
model = Sequential()
model.add(LSTM(50, return_sequences=True, input_shape=(x_train.shape[1], 1)))
model.add(LSTM(50, return_sequences=False))
model.add(Dense(25))
model.add(Dense(1))

#Compilation of model
model.compile(optimizer= 'adam', loss='mean_squared_error')

#Training of model
model.fit(x_train, y_train, batch_size=1,epochs=1)

#Creation of training data set and new array containing scaled values from 1002 to 1062 (Previous 60 closing price values)
test_data = scaled_data[length_training_data - 60: , :]
#Creation of data sets x_test and y_test (Allows test data to use those 60 previous closing values)
x_test = []
y_test = newDataset[length_training_data:, :]
for i in range(60, len(test_data)):
    x_test.append(test_data[i-60:i, 0])
    
#Conversion of data into numpy array
x_test = np.array(x_test)

#Reshape of test data for usability (Same process as earlier with our training data)
x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))

#Obtain model's predicted price values
predictedValues = model.predict(x_test)
predictedValues = scale.inverse_transform(predictedValues)

#Obtain the RMSE (Root Mean Squared Error) (Measures average magnitude of error)
RMSE = np.sqrt(np.mean(predictedValues - y_test)**2)

#Displays a visualization to see 
train = newData[:length_training_data]
valid = newData[length_training_data:]
valid['Predictions'] = predictedValues
#Plot visualization
plt.figure(figsize=(18,9))
plt.title('Google Stock Market')
plt.xlabel('Year')
plt.ylabel('Closing Price in USD', fontsize = 16)
plt.plot(train['Close'])
plt.plot(valid[['Close', 'Predictions']])
plt.legend(['Training Data', 'Actual Stock Value', 'Predicted Stock Value'], loc='lower right')
plt.show()

# Show actual prices vs predicted prices
valid

#The following is done to obtain the predicted value 
pred_google_quote = web.DataReader('GOOG', data_source = 'yahoo', start='2015-01-01', end = '2020-04-10')
#Creation of new data frame
newDF = pred_google_quote.filter(['Close'])
#Obtain previous 60 days of closing price values and convert dataframe into an array
prev60days = newDF[-60:].values
#Scale data in order to have values between 0 and 1
prev60days = scale.transform(prev60days)
#Creation of empty list
x_test = []
#Append last 60 days
x_test.append(prev60days)
#Conversion of x_test set to numpy array
x_test = np.array(x_test)
#Reshape data 
x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))
#Obtain predicted price values
predictedValues = model.predict(x_test)
predictedValues = scale.inverse_transform(predictedValues)
print(predictedValues)

#Obtain actual value for comparison with previous predicted value
actual_google_quote = web.DataReader('GOOG', data_source = 'yahoo', start = '2020-04-13', end = '2020-04-13')
print(actual_google_quote)
