#coding:utf-8

import requests
import re

url = "http://m.ip138.com/ip.asp?ip="
try:
    r = requests.get(url + input())
    content = r.text
    # print(content)
    result = re.findall(r'<p class="result">参考数据一：(.*?)</p>',content)
    for each in result:
        print(each)
except Exception as e:
    print(e)
    pass