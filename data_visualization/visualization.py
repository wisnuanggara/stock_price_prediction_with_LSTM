import plotly.graph_objects as go
from utils.custom_logging import set_logging

def plot_data(data):
    """ Plot the data to time series plot"""
    set_logging("INFO", "Visualize Data...")
    figure = go.Figure(data=[go.Candlestick(x=data["Date"],
                                            open=data["Open"],
                                            high=data["High"],
                                            low=data["Low"],
                                            close=data["Close"])])
    figure.update_layout(title = "Apple Stock Price Analysis",
                         xaxis_rangeslider_visible=False)
    return figure.show()