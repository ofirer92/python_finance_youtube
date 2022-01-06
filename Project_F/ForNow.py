import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
import pandas_datareader.data as web
import pandas as pd


style.use('ggplot')
# start = dt.datetime(2010,1,1)
# end = dt.datetime.today()

# df =web.DataReader('TSLA','yahoo',start,end)
# print(df.tail())
# print(df.columns)

# create csv out of Data frame!
# df.to_csv('tsla.csv'
df = pd.read_csv('tsla.csv',parse_dates=True,index_col=0)
df[['Open','Close']].plot()
plt.show()



