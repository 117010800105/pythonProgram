from NetSpider import *
from bs4 import BeautifulSoup
import requests
import re

def getShitiUrlList():
    urlList = []
    preurl = 'http://www.en8848.com.cn/kt/xiaoxue/read-practice/'
    url = ['index_2.html','index.html']
    for u in url:
        text = getHTMLText(preurl+u,coding='utf-8')
        soup = BeautifulSoup(text,"html.parser")
        items = soup.find_all('a',{'title':re.compile('阅读理解练习题')})
        for item in items:
            urlList.append(item.attrs['href'])

    return urlList

def downloadShiTi(url,saveFileName,answerFileName):
    text = getHTMLText(url,coding='utf-8')
    soup = BeautifulSoup(text,'html.parser')
    title = soup.find('title')
    if( type(title) == 'NoneType'):
        print(url + " was not accessable")
        return
    strtitle = title.string
    strtitle = strtitle[0: strtitle.find('_')]

    item = soup.find('div',{'id':'articlebody'})
    s = str(item)
    k = s.find('答案')
    if k != -1:
        answer = s[k:k+8]
    else:
        answer = ''

    s = s[0:k]
    tag = ['<p>','</p>','</div>','<div>','<div(.*)>','<strong>']
    for t in tag:
        re_tag = re.compile(t)
        s = re_tag.sub(' ',s)
    re_br = re.compile("<br/>")
    s = re_br.sub('\n',s)
    with open(saveFileName,'a+',encoding='utf-8') as fw:
        fw.write(strtitle + '\n')
        fw.write(s + '\n')

    with open(answerFileName,'a+',encoding='utf-8') as fw2:
        fw2.write(strtitle + '\n')
        fw2.write(answer + '\n')

def main():
    urlList = getShitiUrlList();
    for url in urlList:
        print('download from:' + url)
        downloadShiTi(url,'readandcomp.txt','answer.txt')

main()