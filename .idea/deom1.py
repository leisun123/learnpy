# -*-coding:utf-8-*-

import requests
def getHTMLText(url):
    try:
        r = requests.get(url,timeout=30)
        r.raise_for_status() #如果状态不是200，引发HTTPError异常
        r.encoding = r.apparent_encoding
        print(r.request.headers)
        # r = requests.head(url)
        print(r.text[:900])
    except:
        return "产生异常"

if __name__ == "__main__":
    url = "https://item.jd.com/2967929.html"
    getHTMLText(url)