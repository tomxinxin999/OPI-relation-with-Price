import mplfinance as mpf
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.widgets import MultiCursor

kline = pd.read_excel("e:\\Temp\\zl401.xlsx",sheet_name='Sheet1',index_col=0, parse_dates=True)
kline.index.name='Date'
opi0 = mpf.make_addplot(kline['IX_OPI'])
mgl1=mpf.make_addplot(kline['LongPs'], type='bar',color = 'r',width=0.5,panel=1)
mgs1=mpf.make_addplot(kline['ShortPs'], type='bar',color = 'g',width=0.5,panel=2,secondary_y=False)
#opix = mpf.make_addplot(kline['IX_OPI'],type='bar',color = 'y',width=0.5,panel=3)
fig, ax = mpf.plot(kline, type='candle',addplot=[mgl1,mgs1],returnfig=True)###
##multi = MultiCursor(fig.canvas, ax, color='r', lw=0.5, horizOn=False, vertOn=True)
mpf.show()
