from NetSpider import *
from bs4 import BeautifulSoup
import re

def getBaiduPicBtHeadless(url, desurl):
    browser = webdriver.Firefox()
    browser.get(url)
    lis = browser.find_elements(By.CLASS_NAME, "imgitem")
    for li in lis:
        print(li.get_attribute('data-objurl'))
        downloadImageFile(li.get_attribute('data-objurl'), desurl)
    browser.quit()


def getMorePages(kw, pages):
    params = []
    for i in range(30, 30*pages+30, 30):
        params.append({
                          'ipn': 'rj',
                          'ct': 201326592,
                          'is': '',
                          'fp': 'result',
                          'queryWord': kw,
                          'cl': 2,
                          'lm': -1,
                          'ie': 'utf-8',
                          'oe': 'utf-8',
                          'adpicid': '',
                          'st': -1,
                          'z': '',
                          'ic': 0,
                          'word': kw,
                          's': '',
                          'se': '',
                          'tab': '',
                          'width': '',
                          'height': '',
                          'face': 0,
                          'istype': 2,
                          'qc': '',
                          'nc': 1,
                          'fr': '',
                          'pn': i,
                          'rn': 30,
                          'gsm': '1e',
                          '1528253616462': ''
                      })
    url = 'https://image.baidu.com/search/acjson?tn=resultjson_com'
    datalist = []

    for param in params:
        dj = requests.get(url, params=param).json()
        data = dj['data']
        if data is not None and len(data) > 0:
            datalist.append(data)
    return datalist


def main(kw, pages, desurl):
    datalist = getMorePages(kw, pages)
    index = 1
    for data in datalist:
        for i in data:
            if i.get('thumbURL') is not None:
                ir = i.get('thumbURL')
                downloadImageFile(ir, desurl, str(index)+'.jpg')
                index = index + 1

main('范冰冰',3, 'e:/baidupic')