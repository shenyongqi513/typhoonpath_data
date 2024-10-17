import requests
import re

# 台风数据的URL
url2 = 'https://typhoon.weather.com.cn/data/typhoonFlash/taifeng1.xml'

response = requests.get(url2)
data = response.text  # 获取响应内容的文本形式

pattern = r'code="(.+)"  title="(.+)" data="(.+)" city'
# 匹配的结果
results = re.findall(pattern, data)

# 创建列表来保存台风编号
taifengcode = []

# 将结果转换为列表，并提取台风编号
for i in range(len(results)):
    results[i] = list(results[i])  # 每个结果转换为列表
    taifengcode.append(results[i][0])  # 编号数据保存到taifengcode列表

# 构造新的URL并获取日期、时间、经纬度数据
for i in range(len(taifengcode)):
    url = 'https://typhoon.weather.com.cn/data/typhoonFlash/'
    url = url + str(taifengcode[i]) + '.xml'  # 拼接完整的URL

    data = requests.get(url).text

    pattern = r'y="(\d+)" m="(\d+)" d="(\d+)" h="(\d+)" t="(\d+)" jd="([^"]+)" wd="([^"]+)"'
    result = re.findall(pattern, data)


    txtname = str(taifengcode[i]) + '.txt'  # 创建文件名
    with open(txtname, 'w') as f:  # 打开文件进行写入
        for j in result:
            # 仅将日期、时间、经度、纬度写入文件，格式为 y-m-d h:t  (jd,wd)
            f.write(f"{j[0]}-{j[1]}-{j[2]} {j[3]}:{j[4]}  ({j[5]},{j[6]})")
            f.write('\n')
