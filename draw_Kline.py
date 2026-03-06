import pandas as pd
from tqsdk import TqApi
from tqsdk.plotting import TqPlot

# 1. 读取本地K线CSV文件
# 文件路径：e:\temp\klin.csv 注意windows路径写法
df = pd.read_csv(r"E:\temp\MA605_Kline.csv")

# 2. 【关键】数据预处理（必须做，天勤绘图的硬性格式要求）
# 2.1 时间列转成 天勤识别的datetime格式（核心步骤，否则绘图无数据）
df["datetime"] = pd.to_datetime(df["datetime"])
# 2.2 可选：如果csv里的列名是中文（如 开盘价/收盘价），执行下面这行重命名，和英文对应
# df.rename(columns={"开盘价":"open","收盘价":"close","最高价":"high","最低价":"low","成交量":"volume"}, inplace=True)
# 2.3 可选：确保数值列是浮点型，避免绘图异常
num_cols = ["open", "close", "high", "low"]
if "volume" in df.columns:
    num_cols.append("volume")
df[num_cols] = df[num_cols].astype(float)

# 3. 初始化天勤环境并绘图
api = TqApi(web_gui=True)  # web_gui=True 启动网页版K线图（推荐，交互性强）
# 创建绘图对象，传入本地K线DataFrame
plot = TqPlot(df, name="本地klin.csv K线数据")

# 4. 保持绘图窗口打开
api.wait_closed()
