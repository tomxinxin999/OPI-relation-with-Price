import mplfinance as mpf
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 1. 读取数据
df = pd.read_csv(r"e:\temp\kline.csv")

# 2. 处理时间列
df['datetime'] = pd.to_datetime(df['datetime'])
df.set_index('datetime', inplace=True)

# 3. 自定义颜色方案
# 创建自定义样式，下跌K线用青色，上涨K线用红色
mc = mpf.make_marketcolors(
    up='red',           # 上涨K线颜色
    down='cyan',        # 下跌K线颜色 - 改为青色
    edge='inherit',     # 边缘颜色继承
    wick='inherit',     # 影线颜色继承
    volume='in',        # 成交量颜色与K线方向一致
    ohlc='i'            # OHLC线条颜色与K线方向一致
)

# 4. 创建黑色背景样式
s = mpf.make_mpf_style(
    base_mpf_style='charles',  # 基本样式
    marketcolors=mc,
    rc={
        'axes.facecolor': 'black',     # 坐标轴背景色
        'figure.facecolor': 'black',   # 图形背景色
        'grid.color': 'gray',          # 网格线颜色
        'grid.alpha': 0.3,             # 网格线透明度
        'axes.labelcolor': 'white',    # 坐标轴标签颜色
        'axes.edgecolor': 'white',     # 坐标轴边缘颜色
        'xtick.color': 'white',        # X轴刻度颜色
        'ytick.color': 'white',        # Y轴刻度颜色
        'text.color': 'white',         # 文本颜色
    },
    gridcolor='gray',
    gridstyle='-',
    gridaxis='both'
)

# 5. 创建图形和轴 - 使用英文标题和标签
fig, axes = mpf.plot(df, 
                     type='candle',  # 蜡烛图
                     style=s,        # 使用自定义样式
                     title='K-Line Chart',  # 英文标题
                     ylabel='Price',  # 英文标签
                     ylabel_lower='Volume',  # 英文标签
                     volume=True,    # 显示成交量
                     figratio=(12, 8),  # 图表比例
                     figscale=1.2,   # 缩放
                     returnfig=True)  # 返回fig和axes对象以便后续操作

# 解包axes
if isinstance(axes, (list, np.ndarray)):
    ax_main = axes[0]  # 主图（K线图）
    ax_volume = axes[2] if len(axes) > 2 else None  # 成交量图
else:
    ax_main = axes
    ax_volume = None

# 6. 优化鼠标跟随竖线的实现 - 使用英文标签
class FastCursor:
    def __init__(self, ax_main, ax_volume=None):
        self.ax_main = ax_main
        self.ax_volume = ax_volume
        self.fig = ax_main.figure
        
        # 创建竖线对象（但不立即显示）
        self.vline_main = ax_main.axvline(x=0, color='white', linestyle='-', 
                                          linewidth=1, alpha=0.8, visible=False)
        self.vline_volume = None
        
        if ax_volume is not None:
            self.vline_volume = ax_volume.axvline(x=0, color='white', linestyle='-', 
                                                  linewidth=1, alpha=0.8, visible=False)
        
        # 创建价格标签 - 使用英文
        self.price_label = ax_main.text(0.02, 0.97, '', transform=ax_main.transAxes,
                                        bbox=dict(boxstyle="round,pad=0.3", 
                                                  facecolor="yellow", 
                                                  alpha=0.8, edgecolor='black'),
                                        fontsize=9, color='black', visible=False)
        
        # 存储数据
        self.data = df
        
        # 连接事件
        self.fig.canvas.mpl_connect('motion_notify_event', self.on_mouse_move)
        self.fig.canvas.mpl_connect('axes_leave_event', self.on_axes_leave)
        
        # 记录上一次更新的位置，减少不必要的重绘
        self.last_x = None
        
    def on_mouse_move(self, event):
        """鼠标移动事件处理 - 优化响应速度"""
        # 检查鼠标是否在相关坐标轴内
        if event.inaxes != self.ax_main and (self.ax_volume is None or event.inaxes != self.ax_volume):
            self.hide_cursor()
            return
        
        # 获取鼠标的x坐标
        x = event.xdata
        if x is None:
            return
        
        # 使用四舍五入取整，减少位置变化导致的频繁重绘
        x_rounded = round(x)
        
        # 如果位置变化很小，不更新（进一步减少重绘）
        if self.last_x is not None and abs(x_rounded - self.last_x) < 0.1:
            return
        
        self.last_x = x_rounded
        
        # 更新竖线位置
        self.vline_main.set_xdata([x, x])
        self.vline_main.set_visible(True)
        
        if self.vline_volume is not None:
            self.vline_volume.set_xdata([x, x])
            self.vline_volume.set_visible(True)
        
        # 获取并显示当前K线数据 - 使用英文
        x_index = int(x_rounded)
        if 0 <= x_index < len(self.data):
            kline_data = self.data.iloc[x_index]
            date_str = self.data.index[x_index].strftime('%Y-%m-%d')
            price_info = (f"Date: {date_str}\n"
                         f"Open: {kline_data['open']:.2f} | "
                         f"High: {kline_data['high']:.2f}\n"
                         f"Low: {kline_data['low']:.2f} | "
                         f"Close: {kline_data['close']:.2f}\n"
                         f"Volume: {kline_data['volume']:,.0f}")
            
            self.price_label.set_text(price_info)
            self.price_label.set_visible(True)
        
        # 直接重绘，但只重绘必要的区域
        self.fig.canvas.draw_idle()
    
    def on_axes_leave(self, event):
        """鼠标离开坐标轴时的事件处理"""
        self.hide_cursor()
    
    def hide_cursor(self):
        """隐藏光标"""
        self.vline_main.set_visible(False)
        if self.vline_volume is not None:
            self.vline_volume.set_visible(False)
        self.price_label.set_visible(False)
        self.fig.canvas.draw_idle()

# 创建光标对象
cursor = FastCursor(ax_main, ax_volume)

# 设置图形背景色为黑色
fig.patch.set_facecolor('black')
ax_main.set_facecolor('black')
if ax_volume is not None:
    ax_volume.set_facecolor('black')

# 调整标题颜色为白色，使其在黑色背景下可见
if ax_main.get_title():
    ax_main.set_title(ax_main.get_title(), color='white')

# 调整子图间距
plt.subplots_adjust(hspace=0.1)

# 显示图形
plt.show()
