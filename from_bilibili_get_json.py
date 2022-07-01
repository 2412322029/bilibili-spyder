import requests,json
headerbili={
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
        (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.50",
        "referer":"https://www.bilibili.com"
    }

'''
next:页数
oid:视频av号
'''
def get_json(page):
    url="https://api.bilibili.com/x/v2/reply/main?jsonp=jsonp&next=%d&type=1&oid=13662970"
    data = requests.get(url % page, headers=headerbili).text.encode("utf8")
    comm=json.loads(data)
    print(comm)
    '''
    其中ensure_ascii用来规定返回值是否可以包含非ASCII码。
    中文超过ASCII码范围，修改ensure_ascii参数值
    '''
    with open("./json/{}.json".format(page),"w" ,encoding='utf-8') as f:
        f.write(json.dumps(comm, ensure_ascii=False))

for i in range(100):#100页
    get_json(i)
    print(i,'\n')


# vedioreg = 'class="tap-router">(.*?)</a>'
# aurllist = re.findall(vedioreg, rank, re.S | re.M)
# print(aurllist)
