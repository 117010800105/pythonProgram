from NetSpider import *
from bs4 import BeautifulSoup
import re

def getMMPicList():
    page1 = 'https://baike.baidu.com/pic/%E6%9D%9C%E4%B9%94/35172/'
    album_id='4772475'
    imgid = '29381f30e924b89913032ce96c061d950a7bf620'
    page2 = '?fr=newalbum#aid='
    page3 = '&pic='
    pageUrl = page1 + album_id + '/' + imgid + page2 + album_id + page3 + imgid
    text = getHTMLText(pageUrl,'utf-8')
    while True:
        soup = BeautifulSoup(text,'html.parser')
        img_list = soup.find_all('a', {'class': re.compile('pic-item')})
        for img in img_list:
            url = img.attrs['href']
            getMMPic(url)
        next_album = soup.find('a',{'class':'next-album'})
        album_id = next_album['data-album']
        if album_id:
            next_img = next_album.find('img')
            imgsrc = next_img['src']
            imgid = imgsrc.split('/')[-1].split('.')[0]
            next_page = page1 + album_id + '/' + imgid + page2 + album_id + page3 + imgid
            text = getHTMLText(next_page,'utf-8')
        else:
            break


def getMMPic(url):
    text = getHTMLText('https://baike.baidu.com'+ url,'utf-8')
    soup = BeautifulSoup(text,'html.parser')
    url= soup.find('img',{'id':'imgPicture'})
    downloadImageFile(url['src'],'F:/360Downloads/baidupic')


def main():
    getMMPicList()


main()


