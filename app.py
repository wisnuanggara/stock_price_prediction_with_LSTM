from utils.custom_logging import set_logging
from data.yfinance_data import get_yfinance_data
from data_visualization.visualization import plot_data
from exploratory_data_analysis.eda import get_correlation
from model.lstm import *
import numpy as np

if __name__ == '__main__':
    set_logging('INFO', 'Application started...')

    #1 Get stock market data
    data = get_yfinance_data()

    #2 Visualize the data
    print(plot_data(data))

    #3 Get correlation between columns
    col = "Close"
    print(get_correlation(data, col))

    #4 reshape the data
    x,y = reshape_data(data)

    #5 split_data
    xtrain, xtest, ytrain, ytest = split_data(x, y)

    #6 create lstm model
    model = modeling_lstm(xtrain, ytrain)

    #7 predict with new dummy data
    features = np.array([[177.089996, 180.419998, 177.070007, 74919600]])
    print(model_predict(features))

    set_logging('INFO', 'Application terminated...')





