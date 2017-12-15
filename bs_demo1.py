#coding:utf-8

from bs4 import BeautifulSoup
import requests

# demo = open("./demo.html").read()
demo = requests.get("https://python123.io/ws/demo.html")
# demo.encoding = demo.apparent_encoding
# print(demo.text)
soup = BeautifulSoup(demo.content, "html.parser")
print(type(soup.a.next_siblings))