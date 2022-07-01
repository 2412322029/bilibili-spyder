import json,csv

comment=[]#评论列表
for e in range(100):
    with open("./json/{}.json".format(e),"r",encoding="utf8") as f:
        data=json.load(f)
    for i in range(20):
        comment.append(data["data"]["replies"][i]["content"]["message"])
with open("comment.txt","w",encoding="utf8") as fp:
    writer = csv.writer(fp)
    writer.writerow(comment)
    print("写入", comment)#评论的txt文件