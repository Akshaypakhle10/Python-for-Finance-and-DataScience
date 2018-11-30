import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
sns.set_style('whitegrid')
import pandas_datareader as pdr

start_date = "2010/01/01"

AAPL = pdr.DataReader('AAPL',"yahoo",start_date)
GOOG = pdr.DataReader('GOOG', "yahoo",start_date)
MSFT = pdr.DataReader('MSFT', "yahoo",start_date)
AMZN = pdr.DataReader('AMZN', "yahoo",start_date)

# print AAPL.head()
AAPL['Adj Close'].plot()