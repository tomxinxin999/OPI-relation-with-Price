from tqsdk import TqApi, TqAuth
import datetime
import pandas as pd

contract_code="CZCE.AP605"
# 1. 初始化天勤API（无需实盘账户，匿名登录即可获取日线数据）
api = TqApi(web_gui=True, auth=TqAuth("13910926112", "riit1234"))

# 2. 获取RM605合约的日线数据
plt =  pd.read_csv(r"E:\TradeHistory\CZE_old\Kline\MA603_Kline.csv")


klines = api.get_kline_serial(
    symbol=contract_code,
    duration_seconds=24*60*60,  # 24小时=86400秒 → 日线数据
    data_length=50           # 获取最大10000根K线，足够覆盖该合约全部日线
)
cols_to_replace = ['open', 'high', 'low', 'close', 'volume', 'close_oi', 'symbol']
klines[cols_to_replace] = plt[cols_to_replace].head(50).values

while True:
    api.wait_update()


