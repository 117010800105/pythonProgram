import requests
from bs4 import BeautifulSoup
import re

#Craw MM

allMM = []
siteURL = 'http://mm.taobao.com/json/request_top_list.htm'

#获取索引页面的内容
def getHTMLText(pageIndex):
    url = siteURL + "?page=" + str(pageIndex)
    try:
        r = requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding = 'uft-8'
        return r.text
    except:
        return ""

#获取索引页面所有MM的信息,list格式
def fillMMList(soup):
    pattern = re.compile('<div class="list-item".*?pic-word.*?<a href="(.*?)".*?<img src="(.*?)".*?<a class="lady-name.*?>(.*?)</a>.*?<strong>(.*?)</strong>.*?<span>(.*?)</span>',re.S)
    data = soup.find_all(pattern)
    for item in data:
        allMM.append([item[0],item[1],item[2],item[3],item[4]])

#获取MM个人详情页面

#输出
def printMM():
    for mm in allMM:
        print('{:^4}{:^10}{:^5}{:^8}{:^10}'.format(mm[0],mm[1],mm[2],mm[3],mm[4])) 
        

def main():
    url = 'http://mm.taobao.com/json/request_top_list.htm'
    html = getHTMLText(url)
    print(html)
    soup = BeautifulSoup(html,"html.parser")
    fillMMList(soup)
    print(len(allMM))
    printMM()

main()
