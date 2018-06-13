
import itchat

#登录朋友圈
def login():
    itchat.login()
    friends=itchat.get_friends(update=True)[0:]
    return friends

#获取朋友圈数据
def get_var(var, friends):
    variable = []
    for i in friends:
        value = i[var]
        variable.append(value)
    return variable

#朋友圈性别比例
def analyseGender(friends):
    male=female=other=0
    sexes = get_var('Sex', friends)
    for sex in sexes:
        if sex == 1:
            male += 1
        elif sex == 2:
            female += 1
        else:
            other += 1

    total = len(friends[1:])
    malecol = round( float(male)/total * 100, 2)
    femalecol = round( float(female)/total * 100, 2)
    othercol = round( float(other)/total * 100, 2)

    print('男性好友：{:.2f}%%'.format( malecol))
    print('女性好友：{:.2f}%%'.format( femalecol))
    print('不明性别好友：{:.2f}%%'.format( othercol))

    #plot code
    import numpy as np
    import matplotlib.pyplot as plt
    import matplotlib as mpl
    mpl.rcParams['font.sans-serif']=['SimHei']
    mpl.rcParams['axes.unicode_minus'] = False

    map = {
        'Female':(malecol, '#7199cf'),
        'Male': (femalecol, '#4fc4aa'),
        'other': (othercol, '#e1a7a2')
    }
    fig = plt.figure( figsize=(5,5))
    ax = fig.add_subplot(111)
    ax.set_title( '朋友圈性别')

    xticks = np.arange(3) + 0.15
    bar_width = 0.5
    names = map.keys()
    values = [ x[0] for x in map.values()]
    colors = [ x[1] for x in map.values()]

    #柱状图
    bars = ax.bar( xticks, values, width=bar_width, edgecolor='none')
    ax.set_ylabel('比例')
    ax.set_xlabel('性别')
    ax.grid()
    ax.set_xticks( xticks)
    ax.set_xticklabels( names)
    ax.set_xlim( [bar_width/2 - 0.5, 3 - bar_width/2])
    ax.set_ylim( [0, 100])
    for bar, color in zip( bars, colors):
        bar.set_color( color)
        height = bar.get_height()
        plt.text( bar.get_x(), bar.get_height()/4.+ height, '{:.2f}%'.format( float(height)))
    plt.show()

    #饼状图
    fig1 = plt.figure( figsize=(5,5))
    ax = fig1.add_subplot(111)
    ax.set_title('饼图')
    labels = ['{}\n{}%'.format(name, value) for name, value in zip( names, values)]
    ax.pie(values, labels=labels, colors=colors)
    plt.show()

def analyseProvince(friends):
    
"""
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
"""
def main():
    friends = login()
    analyseGender(friends)
    #analyseProvince(friends)
    #analyseSingure(friends)

main()