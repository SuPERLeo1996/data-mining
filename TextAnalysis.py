import jieba
import sys
import matplotlib.pyplot as plt
from wordcloud import WordCloud

text = open('data.txt', encoding='utf-8').read()
print(type(text))
word_list = jieba.cut(text, cut_all=False)

wl_space_split = " ".join(word_list)
print(wl_space_split)

my_word_cloud = WordCloud().generate(wl_space_split)

# 显示词云图
plt.imshow(my_word_cloud)
# 是否显示x轴、y轴下标
plt.axis("off")
plt.show()
