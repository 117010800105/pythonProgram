from NetSpider import *
from bs4 import BeautifulSoup
import re

def getTestpaper(pageUrl,destUrl):
    text = getHTMLText(pageUrl)
    while True:
        soup = BeautifulSoup(text,"html.parser")
        item = soup.find_all('img',{'alt':re.compile('小升初')})
        src = item[0].attrs['src']
        downloadImageFile(src,destUrl)

        nextpage = soup.find('a',string='下一页')
        url = nextpage.attrs['href']
        if url.endswith('shtml'):
            text = getHTMLText(nextpage.attrs['href'])
        else:
            break
    
                                 
    
