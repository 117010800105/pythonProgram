import requests
from bs4 import BeautifulSoup

#Craw MM

allMM = []
siteURL = 'http://mm.taobao.com/json/request_top_list.htm'

#获取索引页面的内容
def getHTMLText(pageIndex):
    url = siteRUL + "?page=" + str(pageIndex)
    try:
        r = requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding = 'uft-8'
        return r.text
    except:
        return ""

#获取索引页面所有MM的信息,list格式
def fillMMList(soup):
    data = soup.find_all('tr')
    for tr in data:
        ltd = tr.find_all('td')
        if len(ltd) == 0:
            continue
        singleUniv = []
        for td in ltd:
            singleUniv.append(td.string)
        allUniv.append(singleUniv)

def printUnivList(num):
    print("{:^4}{:^10}{:^5}{:^8}{:^10}".format("排名",\
            "学校名称","省市","总分","培养规模"))
    for i in range(num):
        u = allUniv[i]
        print("{:^4}{:^10}{:^5}{:^8}{:^10}".format(u[0],\
                u[1],u[2],u[3],u[6]))

def main(num):
    url = 'http://mm.taobao.com/json/request_top_list.htm'
    html = getHTMLText(url)
    soup = BeautifulSoup(html,"html.parser")
    fillUnivList(soup)
    print(len(allUniv))
    printUnivList(num)

main(10)
