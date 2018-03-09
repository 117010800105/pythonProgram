#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 19:01:35 2018

@author: weizhong
"""

from NetSpider import *
from bs4 import BeautifulSoup
import requests

def getMp3(pageUrl, destUrl):
    text = getHTMLText(pageUrl,'gbk')
    soup = BeautifulSoup(text, "html.parser")
    item = soup.find('a',{'id':'dload'})
    mp3url = item.attrs['href']
    print('Download mp3 file:{}'.format(mp3url))
    mp3filename = mp3url.split('/')[-1]
    r = requests.get(mp3url, stream=True)
    with open(destUrl + "/" + mp3filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size = 1024):
            if chunk:
                f.write(chunk)
                f.flush()
        f.close()
    item2 = soup.find('a',{'id':'dloadword'})
    lrcurl = item2.attrs['href']
    lrcfilename = lrcurl.split('/')[-1]
    print('Download lrc file:{}'.format(lrcurl))
    r = requests.get(lrcurl,stream=True)
    with open(destUrl + "/" + lrcfilename, 'wb') as f:
        for chunk in r.iter_content(chunk_size = 1024):
            if chunk:
                f.write(chunk)
                f.flush()
        f.close()
    return r.status_code

pageUrl1 = 'http://www.en8848.com.cn/e/action/down.php?classid=12396&id=' # +urlid
pageUrl2 = '&mp3=http://mp3.en8848.com/xiaoxue/wyxbz3/6b-201601/' #+mp3 name



text = getHTMLText('http://www.en8848.com.cn/xiaoxue/wyxbz/6b2016/','gbk')
soup = BeautifulSoup(text,'html.parser')
item = soup.find_all('ul',{'class':'ch_li6'})
k = 0
for t in item:
    k = k+1
    if k%3 != 0:
        a = t.find('a'); #<a href="/xiaoxue/wyxbz/6b2016/5377.html" title="外研社小学英语三起点六年级下册Module 1 Unit 1" target="_blank">外研社小学英语三起点六年级下册Module 1 Unit 1</a>
        href = a.attrs['href']
        html = href.split('/')[-1]
        urlid = html.split('.')[0]
        print(urlid)
        title = a.attrs['title']
        unit_name = title.find('Module')
        mu = title[unit_name:].split(' ')
        if int(mu[1])<10:
            mp3url = 'M0'+mu[1]+'U'+mu[-1]
        else:
            mp3url = 'M'+mu[1] + 'U' + mu[-1]
        pageUrl = pageUrl1 + urlid + pageUrl2 + mp3url
        getMp3(pageUrl, '/home/weizhong')
 







