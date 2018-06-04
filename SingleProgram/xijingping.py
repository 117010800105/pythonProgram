from NetSpider import *
from bs4 import BeautifulSoup
import requests

guoNeiJiangHua_first_url = 'http://jhsjk.people.cn/result/8?area=401'
def getUrlList(firstPageUrl):
    text = getHTMLText(firstPageUrl, coding='utf-8')
    soup = BeautifulSoup(text, 'html.parser')
    div = soup.find('div',{'class':'pagination pagination-centered'})


