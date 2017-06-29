from NetSpider import *
from bs4 import BeautifulSoup
import re


def getTestpaper(pageUrl, destUrl):
    text = getHTMLText(pageUrl,'gbk')
    while True:
        soup = BeautifulSoup(text, "html.parser")
        title = soup.find('title')
        
        item = soup.find_all('img', {'alt': re.compile('华杯赛')})
        if len(item) < 1:
            item = soup.find_all('img',{'alt':""})
        src = item[0].attrs['src']
        
        downloadImageFile(src, destUrl,title.string+'.jpg')

        nextpage = soup.find('a', string='下一页')
        url = nextpage.attrs['href']
        if url.endswith('shtml'):
            text = getHTMLText(nextpage.attrs['href'],'gbk')
            print(nextpage.attrs['href'])
        else:
            break

def getHuabeiPaper(pageUrl, destUrl):
    text = getHTMLText(pageUrl,'gbk')
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
                if pageUrl.endswith('shtml'):
                    getTestpaper(pageUrl,destUrl)
                if pageUrl.endswith('.jsp'):
                    title = soup.find('title')
                    downloadImageFile(pageUrl,destUrl,title.string+".jpg")


def getHuabeiPapers(destUrl):
    text = getHTMLText('http://www.aoshu.com/e/20160906/57ce56f736156.shtml','gbk')
    soup = BeautifulSoup(text, "html.parser")
    item = soup.find_all('u')
    for ut in item:
        if ut.string:
            url = ut.find('a').attrs['href']
            if url.endswith('shtml'):
                getHuabeiPaper(url,destUrl)


def getYuwenPapers(destUrl):
    text = getHTMLText('http://www.aoshu.com/e/20160802/57a03307c311f.shtml','gbk')
    soup = BeautifulSoup(text,'html.parser')
    item = soup.find('table')
    ltr = item.find_all('tr')
    for tr in ltr:
        ltd = tr.find_all('td')
        for td in ltd:
            item_a = td.find('a')
            if item_a:
                url = item_a.attrs['href']
                fim = getYuwenImagePaper(url,destUrl)
                if fim == 0:
                    getYuwenTextPaper(url,destUrl)

def getYuwenImagePaper(url,destUrl):
    text = getHTMLText(url,'gbk')
    while True:
        print('{}'.format(url))
        soup = BeautifulSoup(text,'html.parser')
        title = soup.find('title')
        img = soup.find('img',{'alt':re.compile('真题')})
        if img:#试卷是图片格式
            url = img.attrs['src']
            downloadImageFile(url,destUrl,title.string+'.jpg')
        else:
            return 0
        nextpage = soup.find('a', string='下一页')
        url = nextpage.attrs['href']
        if url.endswith('shtml'):
            text = getHTMLText(nextpage.attrs['href'],'gbk')
        else:
            break
    return 1

def getYuwenTextPaper(url,destUrl):
    text = getHTMLText(url,'gbk')
    flag = 0
    while True:
        soup = BeautifulSoup(text,'html.parser')
        if flag == 0:
            fname = destUrl + "/" + soup.find('title').string + '.txt'
            fo = open(fname,'w',encoding='utf-8')
            flag = 1
        lp = soup.find_all('p')
        for p in lp:
            lbr = p.find_all('br')
            if len(lbr) > 2:
                fo.write(p.text)
                fo.flush()

        nextpage = soup.find('a',string='下一页')
        url = nextpage.attrs['href']
        if url.endswith('shtml'):
            text = getHTMLText(url,'gbk')
        else:
            break
    fo.close()

