import pandas as pd
from utils.custom_logging import set_logging
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense, LSTM
from utils.custom_logging import set_logging
import numpy as np

def reshape_data(data):
    set_logging("INFO", "Reshape data...")
    x = data[["Open", "High", "Low", "Volume"]]
    y = data["Close"]
    x = x.to_numpy()
    y = y.to_numpy()
    y = y.reshape(-1, 1)
    return x,y

def split_data(x, y):
    set_logging("INFO", "Split the data...")
    xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.2, random_state=42)
    return xtrain, xtest, ytrain, ytest

def modeling_lstm(xtrain, ytrain):
    set_logging("INFO", "Creating lstm model...")
    model = Sequential()
    model.add(LSTM(128, return_sequences=True, input_shape=(xtrain.shape[1], 1)))
    model.add(LSTM(64, return_sequences=False))
    model.add(Dense(25))
    model.add(Dense(1))
    print(model.summary())
    model.compile(optimizer='adam', loss='mean_squared_error')
    model.fit(xtrain, ytrain, batch_size=1, epochs=30)
    return model

def model_predict(features):
    set_logging("INFO", "Predict data...")
    return model.predict(features)
