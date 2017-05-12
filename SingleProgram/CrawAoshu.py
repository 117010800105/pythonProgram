from NetSpider import *
from bs4 import BeautifulSoup
import re


def getTestpaper(pageUrl, destUrl):
    text = getHTMLText(pageUrl)
    while True:
        soup = BeautifulSoup(text, "html.parser")
        item = soup.find_all('img', {'alt': re.compile('华杯赛')})
        src = item[0].attrs['src']
        downloadImageFile(src, destUrl)

        nextpage = soup.find('a', string='下一页')
        url = nextpage.attrs['href']
        if url.endswith('shtml'):
            text = getHTMLText(nextpage.attrs['href'])
        else:
            break

def getHuabeiPaper(pageUrl, destUrl):
    text = getHTMLText(pageUrl)
    soup = BeautifulSoup(text,"html.parser")
    tr_items = soup.find_all('tr')
    for tr in tr_items:
        ltd = tr.find_all('td')
        if len(ltd) == 0:
            continue
        flag = 0
        for td in ltd:
            if '小' in td.text:
                flag = 1
                continue
            if flag != 1:
                break
            la = td.find_all('a')
            for a in la:
                pageUrl = a.attrs['href']
                getTestpaper(pageUrl,destUrl)



def getHuabeiPapers(destUrl):
    text = getHTMLText('http://www.aoshu.com/e/20160906/57ce56f736156.shtml')
    soup = BeautifulSoup(text, "html.parser")
    item = soup.find_all('u')
    for ut in item:
        if ut.string:
            url = ut.find('a').attrs['href']
            getHuabeiPaper(url,destUrl)