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
r = requests.get(url)
soup = BeautifulSoup(r.content, 'lxml')
div_tag = soup.find('div', class_='top_center_list_2')
all_a = div_tag.find_all('a')
for a in all_a:
    if a is not None:
        title = a['title']
        source = url + a['href']
        r = requests.get(source)
        soup = BeautifulSoup(r.content, 'lxml')
        div = soup.find('div', id='content')
        text = div.text
        pub_date = soup.find('span', id='lblCreateDate').string.split(' ', 2)[1]
        pub_date = datetime.strptime(pub_date, '%Y/%m/%d')
        try:
            describe = text.split('：', 1)[1][:50]
        except IndexError:
            describe = text[:50]
        obj = New.objects.filter(title=title)
        if not obj:
            new = New(title=title, public='教务处', source=source, text=text, type='notices', pub_date=pub_date,
                      describe=describe, img_url=img_src)
            new.save()
            times += 1

print("已更新" + str(times) + "条教务通知。")
