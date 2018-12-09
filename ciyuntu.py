#!/usr/bin/env python 
# -*- coding: utf-8 -*-
import jieba
from wordcloud import WordCloud #注意py文件名不能跟wordcloud重复，否则会出错！！
import matplotlib.pyplot as plt

f = open('C:\\Users\\mcc\\Desktop\\600115.txt','r').read()#读取二进制文件用rb
cut_text = jieba.cut(f)#分词
text = "/".join(cut_text)
wordcloud = WordCloud(font_path="C:\\Windows\\Fonts\\simfang.ttf", background_color="white").generate(text)
plt.figure("词云图") #指定所绘图名称
plt.imshow(wordcloud)# 以图片的形式显示词云
plt.axis("off") #关闭图像坐标系
plt.savefig(r"C:\Users\mcc\Desktop\600115.png",dpi=200) #用反斜杠的话会报错
plt.show()

