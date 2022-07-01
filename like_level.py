import json
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号 #有中文出现的情况，需要u'内容'

like= []
level=[]
for e in range(100):
    with open("./json/{}.json".format(e),"r",encoding="utf8") as f:
        data=json.load(f)
    for i in range(20):
        like.append(data["data"]["replies"][i]["like"])
        level.append(data["data"]["replies"][i]["member"]["level_info"]["current_level"])
print(like,level)
plt.bar(level,like)
plt.xlabel('用户等级')
plt.ylabel('点赞总数')
plt.show()
