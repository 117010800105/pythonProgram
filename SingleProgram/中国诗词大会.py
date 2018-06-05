from bs4 import BeautifulSoup
from NetSpider import getHTMLText

html_text = getHTMLText('http://www.360doc.com/content/17/0619/16/44417620_664485200.shtml',coding='utf-8')
soup = BeautifulSoup(html_text,'html.parser')
shiti = soup.find('td', {'id': 'artContent'})
p_list = shiti.find_all('p')

with open('e:/中国诗词大会题库2017.txt', 'w+') as fr:
    for p in p_list:
        s = p.string
        if '答案' not in s:
            fr.write(s + '\n')
