import pandas as pd
import matplotlib.pyplot as plt
import wordcloud,jieba

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号 #有中文出现的情况，需要u'内容'
#文件目录
file_path="res.csv"
df=pd.read_csv(file_path,encoding="gbk")
#柱状图
def _bar():
    df.columns = ["word","frequency"]
    print(df.head())
    plt.bar(df["word"],df["frequency"])
    plt.xlabel('词')
    plt.ylabel('出现次数')
    plt.show()
_bar()


#词云
with open("comment.txt","r",encoding="utf8")as f:
    txt=f.read()
stopwords = ["的","了","我","时","在","你","看","到","没","不","就","是","人","也","有","和","会",
    "一个","没有","时候","弹幕","自己","什么","时间","知道","就是","现在","真的","已经","还是","这个","看到","可以","因为"
    ,"你们","才能","不是","但是","那个","最后","每秒","所以","他们","觉得","怎么样","一样","可能","举报","这部","大家","不能","当时"
    ,"一直","一次","然后","还有","这样","评论","如果","那么","为什么","第一次","感谢","只是","这些","之后","忘记","一下","虽然","为了"
    ,"一定","今天","这么","不会","这里","去年","两个","以后","地方","那些","这种","怎么","其实","起来","应该","---","发生","只有","天气"
    ,"今年","很多","好像","所有","一部","出来","找到","之子","一遍","谢谢","告诉","东西","永远","的话","五块","一句","之前","过去","一年"
    ,"一天","终于","选择","对于","非常","突然"
]

w=wordcloud.WordCloud(background_color="white",font_path="msyh.ttc",height=600,width=800,stopwords=stopwords)
w.generate(" ".join(jieba.lcut(txt)))
w.to_file("词云.png")
