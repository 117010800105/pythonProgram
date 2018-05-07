from bs4 import BeautifulSoup
import requests

def getHTMLText(url,coding='gbk'):
    try:
        r = requests.get(url,timeout=30)
        print(r)
        r.raise_for_status()
        r.encoding = coding
        return r.text
    except:
        return ""

def downloadImageFile(imgUrl, destUrl):
    local_filename = imgUrl.split('/')[-1]
    print('Download Image File={}'.format(local_filename))
    r = requests.get(imgUrl, stream=True)
    with open(destUrl + "/" + local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size = 1024):
            if chunk:
                f.write(chunk)
                f.flush()
        f.close()
    return r.status_code

def downloadImageFile(imgUrl, destUrl, fname):
    local_filename = imgUrl.split('/')[-1]
    print('Download Image File={}'.format(local_filename))
    r = requests.get(imgUrl, stream=True)
    with open(destUrl + "/" + fname, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
                f.flush()
        f.close()
    return r.status_code