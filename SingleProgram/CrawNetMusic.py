import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from NetSpider import *
from bs4 import BeautifulSoup
import re

allMusics=[]
url = 'http://music.163.com/#/discover/playlist/?order=hot&cat=%E5%85%A8%E9%83%A8&limit=35&offset=0'

def getHTMLTextByHeadless(url):
    broswer = webdriver.Firefox()
    while url != 'javascript:void(0)':
        broswer.get(url)
        broswer.switch_to.frame("contentFrame")
        data = broswer.find_element_by_id("m-pl-container").find_elements_by_tag_name("li")
        for d in data:
            music = []
            nb = d.find_element(By.CLASS_NAME,'nb').text
            if '万' in nb:
                n = nb[:-1]
                if int(n) > 500:
                    music.append(n)
                    al = d.find_elements_by_tag_name('a')
                    title = al[0].get_attribute('title')
                    music.append(title)
                    hr = al[0].get_attribute('href')
                    music.append(hr)
                    author = al[3].get_attribute('title')
                    music.append(author)
                    allMusics.append(music)
        url = broswer.find_element_by_css_selector("a.zbtn.znxt").get_attribute('href')
    broswer.close()


def fillMusicList():
    html = getHTMLText(url, coding='utf-8')
    soup = BeautifulSoup(html,'html.parser')
    ul = soup.find('ul', {'id':'m-pl-container'})
    divs = ul.find_all('div', {'class': re.compile('u-cover')})

    for div in divs:
        music = []
        nb = div.find('span', {'class': 'nb'}).string
        if '万' in nb:
            n = nb[:-1]
            if int(n) > 500:
                music.append(n)
                a = div.find('a')
                title = a.title
                music.append(title)
                hr = musicurl + a.href
                music.append(hr)
                a2 = div.find('a', {'class':re.compile('nm nm-icn f-thide')})
                author = a2.string
                music.append(author)
                allMusics.append(music)

def printMusicList():
    print('{:<8}{:<20}{:<8}{:<20}'.format('下载次数', '歌曲名称', '歌手', '歌曲链接地址'))
    for music in allMusics:
        print('{:<8}{:<20}{:<8}{:<20}'.format(str(music[0]), music[1], music[3], music[2]))

#fillMusicList()
#printMusicList()
getHTMLTextByHeadless(url)
printMusicList()