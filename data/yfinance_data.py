import datetime
import pandas as pd
import yfinance as yf
from datetime import date, timedelta
from utils.custom_logging import set_logging

today = date.today()

d1 = today.strftime("%Y-%m-%d")
end_date = d1

d2 = date.today() - timedelta(days=5000)
d2 = d2.strftime("%Y-%m-%d")
start_date = d2

def get_yfinance_data():
    """ Get yahoo finance data. Yahoo finance provide daily stock market data"""
    try:
        data = yf.download('AAPL',
                           start=start_date,
                           end=end_date,
                           progress=False)
        data["Date"] = data.index
        data = data[["Date", "Open", "High", "Low", "Close",
                     "Adj Close", "Volume"]]
        data.reset_index(drop=True, inplace=True)
        set_logging("INFO", "Get YFinance Data Success !")
        return data
    except Exception as e:
        set_logging("INFO", "Get YFinance Data Failed"+ str(e))
        raise RuntimeError("Get YFinance Data Failed")

