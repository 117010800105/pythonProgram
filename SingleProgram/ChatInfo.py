
import itchat
itchat.login()
friends=itchat.get_friends(update=True)[0:]

#朋友圈性别比例
male=female=other=0
for i in friends[1:]:
    sex=i["Sex"]
    if sex == 1:
        male += 1
    elif sex == 2:
        female += 1
    else:
        other += 1

total = len(friends[1:])
print("男性好友：%2f%%"%(float(male)/total*100)+"\n" +
      "女性好友：%2f%%"%(float(female)/total*100) + "\n" +
      "不明性别好友：%2f%%"%(float(other)/total*100))

#plot code

#朋友圈数据分析
def get_var(var):
    variable = []
    for i in friends:
        value = i[var]
        variable.append(value)
    return variable

NickName = get_var("NickName")
Sex = get_var("Sex")
Province = get_var("Province")
City = get_var("City")
Signature = get_var("Signature")

from pandas import DataFrame
data = {'NickName': NickName, 'Sex': Sex, 'Province': Province, 'City': City, 'Signature': Signature}
frame = DataFrame(data)
frame.to_csv('data.csv',index=True)

#plot code

#朋友圈个性签名词云图
import re
siglist =[]
for i in friends:
    signature = i["Signature"].strip().replace("span","").replace("class","").replace("emoji","")
    rep = re.compile("1f\d+\w*|[<>/=]")
    signature = rep.sub("",signature)
    siglist.append(signature)
text = "".join(siglist)

#第一次运行时将朋友圈内容存入文件

#fout = open('friends.txt','wb')
#pickle.dump(text,fout)
#fout.close()

import pickle
#fr = open('friends.txt','rb')
#text = pickle.load(fr)
#fr.close()

import jieba
wlist = jieba.cut(text, cut_all = True)
counts = {}
for word in wlist:
    if len(word ) == 1:
        continue
    else:
        counts[word] = counts.get(word,0) + 1


import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
import numpy as np
import PIL.Image as Image
coloring = np.array(Image.open("f:/22.jpg"))
wc = WordCloud(background_color="white",
                         max_words=2000,
                         mask=coloring,
                         max_font_size=60,
                         random_state=42,
                         scale=2,
                         font_path="c:/Windows/Fonts/SimHei.ttf")
wc.generate_from_frequencies(counts)
image_colors = ImageColorGenerator(coloring)

plt.imshow(wc)
plt.axis("off")
plt.figure()
plt.show()


