#coding:utf-8

import requests
import os

url = ''#图片地址
root = ''#保存图片地址
path = root + url.split('/')[-1]#储存的图片格式
try:
    if not os.path.exists(root):#判断图片储存目录是否存在
        os.mkdir(root)
    if not os.path.exists(path):#判断图片是否存在
        r = requests.get(url)
        with open(path,'wb') as f:
            f.write(r.content)
            f.close()
            print("文件保存成功")
    else:
        print("文件已存在")
except Exception as e:#错误处理
    print(e)
    print("爬取失败")
    pass