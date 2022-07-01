import jieba,re
#去除标点
def get_text(file_name):
  with open(file_name, 'r', encoding='utf-8') as fr:
    text = fr.read()
    #删除的标点
    del_ch = ['《','，','》','\n','。','、','；','"',\
      '：',',','！','？',' ']
    for ch in del_ch:
      text = text.replace(ch,'')
    return text


file_name = 'comment.txt'
text = get_text(file_name)
vlist = jieba.lcut(text)#调用jieba实现分词，返回列表

res_dict = {}
#进行词频统计
for i in vlist:
  res_dict[i] = res_dict.get(i,0) + 1
res_list = list(res_dict.items())
#print(res_list)
#降序排序
res_list.sort(key = lambda x:x[1], reverse = True)
fin_res_list = []

#去除单个字的词
for item in res_list:
  if(len(item[0])>=2):
    fin_res_list.append(item)
word_list=[]
words=[]
for i in range(1000):
  word,count = fin_res_list[i]
  pstr = str(i+1) + ':'
  word_list.append(word)
  with open('ignore_dict.txt', 'r', encoding='utf-8') as f:
    ignore_words = f.read().splitlines()
    # 遍历分词
    for word in word_list:
      if word not in ignore_words:#排除词
        word = re.sub(r'[\n ]', '', word)
        if len(word) < 1:
          continue
        words.append(word)
  # print(pstr, end=' ')
  # print(words[i], count)
  with open("res.csv","a+")as fa:
    fa.write(str(words[i])+","+str(count)+"\n")
