#-*-coding:utf-8-*-

import requests
kv = {'wd':'Python'}#关键词
r = requests.get("http://www.baidu.com/s",params=kv)
a = r.status_code
b = r.request.url
d = len(r.text)
print(a,b,d)