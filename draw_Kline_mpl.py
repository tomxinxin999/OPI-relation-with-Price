import mplfinance as mpf
import matplotlib.pyplot as plt
import pandas as pd# 1. 读取数据
df = pd.read_csv(r"e:\temp\kline.csv")


# 3. 处理时间列
df['datetime'] = pd.to_datetime(df['datetime'])
df.set_index('datetime', inplace=True)

# 4. 绘制基础K线图
mpf.plot(df, 
         type='candle',  # 蜡烛图
         style='charles',  # 样式
         title='K线图',
         ylabel='价格',
         ylabel_lower='成交量',
         volume=True,  # 显示成交量
         figratio=(12, 8),  # 图表比例
         figscale=1.2)  # 缩放


plt.show()
api.close()
