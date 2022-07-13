import pandas as pd
from utils.custom_logging import set_logging

def get_correlation(data, col):
    """ Get correlation from specific column to other columns in the data"""
    set_logging("INFO", "Get correlation between data...")
    correlation = data.corr()
    return correlation[col].sort_values(ascending=False)