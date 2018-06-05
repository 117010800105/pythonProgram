from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
import time
def getHTMLText(url,coding='gbk'):
    try:
        r = requests.get(url,timeout=30)
        print(r)
        r.raise_for_status()
        r.encoding = coding
        return r.text
    except:
        return ""


def downloadImageFile(imgUrl, destUrl, fname=''):
    local_filename = imgUrl.split('/')[-1]
    print('Download Image File={}'.format(local_filename))
    try:
        r = requests.get(imgUrl, stream=True)
        r.raise_for_status()

        if len(fname) == 0:
            fname = local_filename
        print('fname={}'.format(fname))
        with open(destUrl + "/" + fname, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
                    f.flush()
            f.close()
        return r.status_code
    except:
        return r.status_code


def getHTMLTextByHeadless(url):
    browser = webdriver.Firefox()
    browser.get(url)
    text = browser.page_source
    browser.quit()
    return text

url = 'https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&'\
    'cl=2&lm=-1&st=-1&sf=1&fmq=&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&'\
    'face=0&istype=2&ie=utf-8&fm=index&pos=history&word=%E6%9D%A8%E5%B9%82'
#text = getHTMLText(url)
#print(text)

phantomjs_path = 'E:\\Program Files\\Python\\Python36-32\\Scripts'
pageSource = getHTMLTextByHeadless(url)
pageSource.encode(encoding='utf-8')
with open('e:/source.txt','w') as fr:
    fr.write(pageSource)
