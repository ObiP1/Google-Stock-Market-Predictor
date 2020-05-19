# Google Stock Market Predictor
Utilizes Yahoo finance as an API & retrieves data for use. Implements machine learning with the use of a Recurrent Neural Network in order to provide a prediction of Google stocks. Incorporates visulaization in the form of a table and graph in order to display predicted stock values with actual stock values.

*NOTE: This was an attempt to get as close to the actual values as I possibly could, there is no solid way to predict the stock market with 100% accuracy.*


STEP 1)
The first step is importing the necessary libraries in which we will be using for this project.

![Imports](https://user-images.githubusercontent.com/60532479/82355320-0b4c0480-99d0-11ea-93b3-eff985861a27.png)

STEP 2)
Implement the use of pandas' Datareader by grabbing the necessary information we need. In this case, I am grabbing Google's stocks from Yahoo Finance for the dates of Jan 1, 2015 to April 10, 2020. You can also choose to view the data you are working with by calling back the function afterwards.

![Google df](https://user-images.githubusercontent.com/60532479/82355643-7d244e00-99d0-11ea-829f-e530a1773538.png)

STEP 3)
View the size of your data as a whole

![Google df shape](https://user-images.githubusercontent.com/60532479/82357027-78f93000-99d2-11ea-9646-bc35a28ee326.png)


STEP 4) (Optional)
Visualization of prior closing prices for Google within the stock market.

![PrevPricesGoogle](https://user-images.githubusercontent.com/60532479/82357375-050b5780-99d3-11ea-97df-44023f487741.png)


STEP 5) 
Create a new data frame with only closing price values. Then, convert the data into a numpy array for usability. Lastly, train 80% of the the closing prices. You can then view the size of your training data and confirm that it is in fact 80% of the data which was obtained in Step 3.

![GoogleLen](https://user-images.githubusercontent.com/60532479/82358318-59fb9d80-99d4-11ea-91b1-93be549d5949.png)

STEP 6)
Implement the use of the minMaxScaler and scale the data. Call back the function to confirm the scaling.

![GoogleScale](https://user-images.githubusercontent.com/60532479/82358803-0a69a180-99d5-11ea-8983-18362d9217f8.png)


STEP 7)
Create both a scaled and training dataset. Use the previous 60 closing price values and append them to the x_train dataset. Use the 61st value and append it to the y_train dataset. It is not manadatory, but you can also test what you have so far with the commented code and see what you are working with.




