# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 11:44:38 2018

@author: Administrator
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 14:51:17 2018

@author: Administrator
"""


files={'云海玉弓缘.txt','神雕侠侣.txt','多情剑客无情剑.txt'}
excludes={'“','”','。','-','？','！','，',' ','^p'}
def getDict(fileName):
    txt = open(fileName,'r',encoding='UTF-8').read()
    for ch in excludes:
        txt = txt.replace(ch,"")
    words = list(txt)
    counts = {}
    for word in words:
        counts[word] = counts.get(word,0) + 1
    
    items = list(counts.items())
    items.sort(key=lambda x: x[1], reverse = True)
    print("\n\n{}字频统计结果：".format(fileName))
    for i in range(50):
        if i%6 == 0:
            print("\n")
        word, count = items[i]
        print("{0:<3}{1:>6}".format(word, count), end="  ")
        
    

for f in files:
    getDict(f)

