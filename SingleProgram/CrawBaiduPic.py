from NetSpider import *
from bs4 import BeautifulSoup
import re

def getImg(html):
    imgre = re.compile('"objURL":"(.*?)"')
    imglist = re.findall(imgre,html)
    return imglist
def download(urls,path):
    index = 1
    for url in urls:
        print("Download Image from page:{}".format(url))
        status = downloadImageFile(url,path,str(index)+".jpg")
        try:
            if str(status)[0] == '4':
                print("未下载成功{}".format(url))
                continue
        except Exception as e:
            print("未下载成功{}".format(url))
        index += 1

page = 'https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result' \
       '&fr=&sf=1&fmq=1494981920766_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2' \
       '&ie=utf-8&word=%E5%BC%A0%E9%A6%A8%E4%BA%88&f=3&oq=zhang&rsp=2'
html= getHTMLText(page,'utf-8')
download(getImg(html),'e:/360Downloads/baidupic')

