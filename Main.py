import math
import pandas as pd
import numpy as np
import pandas_datareader as web
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

df = web.DataReader('GOOG', data_source = 'yahoo', start='2015-01-01', end='2020-04-10')

#Creates plot to analyze previous closing values
plt.figure(figsize=(16,8))
plt.title('Previous Closing Prices')
plt.plot(df['Close'])
plt.xlabel('Year',fontsize=20)
plt.ylabel('Price of Stock in USD', fontsize=20)
