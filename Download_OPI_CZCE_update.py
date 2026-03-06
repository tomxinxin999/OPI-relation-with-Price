#2026-1-14 update

import requests
import os
import datetime
# 定义下载链接

# 1. 定义指定变量
type_code = 'RM'  # 目标type变量，两位大写字母
start_date_str = '20250101'  # 起始日期 YYYYMMDD
end_date_str =  '20250531'    # 结束日期 YYYYMMDD

# 2. 日期格式转换：字符串转datetime对象，用于日期遍历
date_format = "%Y%m%d"
#把输入的字符型变量，变成时间类型的变量，
start_date = datetime.datetime.strptime(start_date_str, date_format).date()
end_date  = datetime.datetime.strptime( end_date_str, date_format).date()

# 3. 遍历起始-结束之间的每一天（包含起止当天），拼接并打印URL
current_date = start_date
while current_date <= end_date:
    # 格式化当前日期为 YYYYMMDD 格式的字符串
    current_date_str = current_date.strftime(date_format)
    # 提取当前日期的年份（4位）
    current_year = current_date.year
    # 固定URL模板 + 动态拼接变量
    download_url = f"https://www.czce.com.cn/cn/DFSStaticFiles/Future/{current_year}/{current_date_str}/FutureDataHolding{type_code}.xls"
    # 生成保存每日数据的文件名
    # 构建新的文件名
    Filename = f"{type_code}_OPI_{current_date_str}.xls"
    # 定义本地保存文件夹
    save_folder = r"E:\TradeHistory\CZE_old\DataHold"
    # 构建完整的本地保存路径
    save_path = os.path.join(save_folder, Filename)
    try:
    # 发送请求获取文件，以流的方式下载
        response = requests.get(download_url, stream=True)
    # 检查响应状态码，如果不是 200 则抛出异常
        response.raise_for_status()
    
    # 以二进制写入模式打开本地文件
        with open(save_path, 'wb') as file:
        # 分块写入文件
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    file.write(chunk)

        print(f"文件已成功下载到 {save_path}")
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP 错误发生: {http_err}")
        print(current_date ,'  have no data')
    except requests.exceptions.RequestException as req_err:
        print(f"请求发生错误: {req_err}")
    except Exception as err:
        print(f"发生未知错误: {err}")


    
    # 日期+1天，进入下一次循环
    current_date += datetime.timedelta(days=1)

print("\n✅ 所有日期处理完成！")








##from datetime import datetime, timedelta
##
### 起始日期
##start_date_str = '20250101'
##start_date = datetime.strptime(start_date_str, '%Y%m%d')
##
### 结束日期
##end_date_str = '20250425'
##end_date = datetime.strptime(end_date_str, '%Y%m%d')
##
### 当前日期初始化为起始日期
##current_date = start_date
##
##while current_date <= end_date:
##    # 将日期格式化为字符串
##    current_date_str = current_date.strftime('%Y%m%d')
##    print(current_date_str)
##
##    # 日期加 1 天
##    current_date += timedelta(days=1)
##    
    
