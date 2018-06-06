from NetSpider import *
from bs4 import BeautifulSoup
import re

def getBaiduPic(url, desurl):
    browser = webdriver.Firefox()
    browser.get(url)
    lis = browser.find_elements(By.CLASS_NAME, "imgitem")
    for li in lis:
        print(li.get_attribute('data-objurl'))
        downloadImageFile(li.get_attribute('data-objurl'), desurl)
    browser.quit()

def getMorePages(kw, pages):
    params = []
    for i in range(30,30*pages+30,30):
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
                          'pn': pages,
                          'rn': 30,
                          'gsm': '1e',
                          '1528253616462': ''
                      })
    url = 'https://image.baidu.com/search/acjson?tn=resultjson_com'
    urls = []
    for param in params:
        for key in param.keys():
            url = url + '&' + key + '=' + str(param[key])
        urls.append(url)

    return urls


def main(kw, pages, desurl):
    urls = getMorePages(kw, pages)
    for url in urls:
        getBaiduPic(url,desurl)

main('杨幂',10, 'e:/baidupic')