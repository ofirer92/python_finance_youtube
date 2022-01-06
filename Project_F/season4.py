import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import mplfinance as mp
import matplotlib.dates as mdates
import numpy as np
import pandas_datareader.data as web
import pandas as pd


style.use('ggplot')

df = pd.read_csv('tsla.csv',parse_dates=True,index_col=0)
# df['100Ma'] = df['Adj Close'].rolling(window=100, min_periods=0).mean()

df_ohlc = df['Adj Close'].resample('10D').ohlc()
df_volume = df['Volume'].resample('10D').sum()

df_ohlc.reset_index(inplace=True)
df_ohlc['Date'] = df_ohlc['Date'].map((mdates.date2num)


print(df_ohlc)



ax1 = plt.subplot2grid((6,1), (0,0),rowspan=5,colspan=1)
ax2 = plt.subplot2grid((6,1), (5,0),rowspan=1,colspan=1)

