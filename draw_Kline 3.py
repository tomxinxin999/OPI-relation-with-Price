import pandas as pd
from tqsdk import TqApi, TqKq, TqAuth

# ===================== 1. 读取本地K线CSV文件 =====================
# 文件路径：e:\temp\klin.csv (r前缀防止windows路径转义，必须加)
df = pd.read_csv(r"e:\temp\kline.csv")

# ===================== 2. 【核心必做】数据预处理 =====================
# 天勤加载本地K线的硬性格式要求，缺一不可，按顺序执行
# 2.1 时间列转为标准datetime格式（天勤核心识别条件，无此步必无数据）
df["datetime"] = pd.to_datetime(df["datetime"])
# 2.2 确保K线核心列是浮点型，防止绘图异常
num_cols = ["open", "close", "high", "low", "volume", "OPI"]
df[num_cols] = df[num_cols].astype(float)
api = TqApi(web_gui=True, auth=TqAuth())
klines = api.get_kline_serial(symbol="SHFE.rb2501", duration_seconds=86400)

# ===================== 3. 新版天勤初始化+加载本地数据绘图 =====================
klines["datetime"] = df["datetime"]
klines["open"]     = df["open"]
klines["high"]     = df["high"]
klines["low"]      = df["low"]
klines["close"]    = df["close"]
klines["volume"]   = df["volume"]
# 可选：OPI持仓量也可以赋值，天勤会自动绘制，不需要就删掉这行即可
klines["opi"]      = df["OPI"]
# ===================== 4. 保持绘图窗口常驻 =====================
print("本地K线数据加载成功，浏览器已打开绘图页面，关闭程序则窗口关闭")

