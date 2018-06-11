import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
import numpy as np
import PIL.Image as Image

def cal():
    excludes = {}  # {"将军","却说","丞相"}
    txt = open("三国演义.txt", "r", encoding='utf-8').read()
    words = jieba.lcut(txt)
    counts = {}
    for word in words:
        if len(word) == 1:
            continue
        else:
            counts[word] = counts.get(word, 0) + 1
    for word in excludes:
        del (counts[word])
    items = list(counts.items())
    items.sort(key=lambda x: x[1], reverse=True)
    for i in range(15):
        word, count = items[i]
        print("{0:<10}{1:>5}".format(word, count))
    return counts

def drawWordCloud(counts):
    coloring = np.array(Image.open("E:/baidupic/9.png"))
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
    plt.show()
def main():
    counts = cal()
    drawWordCloud(counts)

main()