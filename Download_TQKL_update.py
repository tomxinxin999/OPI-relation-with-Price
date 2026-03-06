import os
import pandas as pd
from tqsdk import TqApi, TqAuth

# ===================== 配置参数（按需修改这部分即可） =====================
contract_code = "CZCE.RM603"  # RM605合约代码 郑州商品交易所 菜粕605
save_path = r"E:\TradeHistory\CZE_old\Kline"        # 数据保存根目录
file_name = "RM603_Kline.csv" # 保存的文件名
# ========================================================================

# 1. 初始化天勤API（无需实盘账户，匿名登录即可获取日线数据）
api = TqApi(web_gui=True, auth=TqAuth("13910926112", "riit1234"))

# 2. 获取RM605合约的日线数据
klines = api.get_kline_serial(
    symbol=contract_code,
    duration_seconds=24*60*60,  # 24小时=86400秒 → 日线数据
    data_length=200           # 获取最大10000根K线，足够覆盖该合约全部日线
)

# 4. 转换为Pandas的DataFrame格式（数据处理+保存必备，格式规整）
df = pd.DataFrame(klines)
df = df[df['datetime'] != 0]  #清洗日期为0的行
df.drop(columns=['id', 'open_oi', 'duration'], inplace=True) #清洗掉无用的列
df['datetime'] = (pd.to_datetime(df['datetime'], errors='coerce') +
                          pd.to_timedelta(1, unit='d')).dt.strftime('%Y/%m/%d')  #提取日期并向后推迟一天
#转为pandas时间格式，并提取其中中的日期部分
# 5. 拼接完整保存路径 + 保存为CSV文件（最通用的格式，Excel也能直接打开）
full_save_file = os.path.join(save_path, file_name)
df.to_csv(full_save_file, index=False, encoding="utf_8_sig")

# 6. 收尾操作
api.close()
print(f"✅ {contract_code}日线数据下载完成！")
print(f"✅ 数据保存路径：{full_save_file}")
print(f"✅ 共下载到 {len(df)} 根日线K线")
