import requests
import os

# 定义下载链接
download_url = "http://www.czce.com.cn/cn/DFSStaticFiles/Future/2026/20260115/FutureDataHoldingRM.xls"

# 从 URL 中提取日期部分
url_parts = download_url.split('/')    #url_parts is a python list
date = url_parts[-2] #'/' 分割后,倒数第二个部分就是date

# 构建新的文件名
Filename = f"FutureDataHoldingRM{date}.xls"

# 定义本地保存文件夹
save_folder = r"E:\Code_Python\CZE\FileHold"

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
except requests.exceptions.RequestException as req_err:
    print(f"请求发生错误: {req_err}")
except Exception as err:
    print(f"发生未知错误: {err}")



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
    
