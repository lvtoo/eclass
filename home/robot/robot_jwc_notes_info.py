"""
Version: 0.1
Author: lvtoo
e-mail: o@oouul.com
Date: 2018/11/27

"""
import requests
from bs4 import BeautifulSoup
from home.models import New
from datetime import datetime

# 计数，更新了几条数据
times = 0
# 给jwc一个request
url = "http://jwc.shmtu.edu.cn/"
r = requests.get(url+"/jiaowugonggao")
soup = BeautifulSoup(r.content, 'lxml')
div_tag = soup.find('div', class_='table-responsive')
all_a = div_tag.find_all('a')
for k in all_a:
    if k.get('href') is not None:
        title = k.string
        source = url + str(k.get('href'))
        r = requests.get(source)
        soup = BeautifulSoup(r.content, 'lxml')
        div = soup.find('div', class_='region region-content')
        text = div.text
        img_src = ''
        pub_date = soup.find('div', class_="view-content").text.split('：', 2)[2][:10]
        pub_date = pub_date.rstrip()#去除时间右边的空格
        pub_date = datetime.strptime(pub_date, '%Y/%m/%d')
        try:
            describe = text.split('：', 1)[1][:40]
        except IndexError:
            describe = text[:50]
        describe = describe.rstrip()
        obj = New.objects.filter(title=title)
        if not obj:
            new = New(title=title, public='教务处', source=source, text=text, type='notices', pub_date=pub_date,
                      describe=describe, img_url=img_src)
            new.save()
            times += 1

print("已更新" + str(times) + "条教务通知。")
