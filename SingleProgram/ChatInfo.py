
import itchat
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import re
import jieba
import PIL.Image as Image
from wordcloud import WordCloud, ImageColorGenerator

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

    provlist = get_var('Province', friends)
    provdict = {}
    for p in provlist:
        provdict[p] = provdict.get(p,0) + 1
    provdict = sorted(provdict.items(), key= lambda x : x[1], reverse=True)

    #画图
    figpro = plt.figure(figsize=(10,5))
    axpro = figpro.add_subplot(111)
    axpro.set_title('省份')
    xticks = np.linspace(0.5,20,10)
    bar_width = 0.8
    pros= []
    values = []
    count = 0
    for d in provdict:
        pros.append(d[0])
        values.append(d[1])
        count += 1
        if count >= 10:
            break

    colors = ['#FFEC88', '#FFE4C4','#FFC125','#FFB6C1','#CDCDB4','#CDC8B1','#CDB79E','#CDAD00','#CD96CD',\
              '#CD853F']
    bars = axpro.bar( xticks, values, width=bar_width, edgecolor='none')
    axpro.set_ylabel('人数')
    axpro.set_xlabel('省份')
    axpro.grid()
    axpro.set_xticks( xticks)
    axpro.set_xticklabels(pros)
    axpro.set_xlim(0,20)
    axpro.set_ylim([0,100])

    for bar, color in zip( bars, colors):
        bar.set_color(color)
        height = bar.get_height()
        plt.text( bar.get_x()+bar.get_width()/4., height, '{}'.format(height))

    plt.show()


def drawWordcloudPlot(counts):
    coloring = np.array(Image.open("E:/baidupic/alice_color.png"))
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
    plt.savefig('friendSign.jpg')
    plt.show()


def analyseSignature(friends):
    signatures = get_var('Signature', friends)
    siglist = []
    for sign in signatures:
        sign = sign.strip().replace("span", "").replace("class", "").replace("emoji", "")
        rep = re.compile("lf\d+\w*|[<>/=]")
        sign = rep.sub("", sign)
        siglist.append(sign)
    text = "".join(siglist)
    wlist = jieba.cut(text, cut_all=True)
    counts = {}
    for word in wlist:
        if len(word) == 1:
            continue
        else:
            counts[word] = counts.get(word, 0) + 1
    wdict = {}
    i = 0
    for d in counts.items():
        if d[1] > 3:
            wdict[d[0]] = d[1]

    drawWordcloudPlot(wdict)

def main():
    friends = login()
    analyseGender(friends)
    analyseProvince(friends)
    analyseSignature(friends)

main()