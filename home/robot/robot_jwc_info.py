# coding=utf-8
import requests
from bs4 import BeautifulSoup
from home.models import New


# 计数，更新了几条数据
times = 0
# 给jwc一个request
url = "http://jwc.shmtu.edu.cn/"
r = requests.get(url)
soup = BeautifulSoup(r.content, 'lxml')
all_li = soup.find('div', id='marquee1').find('ul').find_all('li')
for li in all_li:
    a = li.find('a')
    if a is not None:
        source = a['href']
        title = a['title']
        source = url + source
        r = requests.get(source)
        soup = BeautifulSoup(r.content, 'lxml')
        text = soup.find('div', id='content').text
        pub_date = soup.find('span', id='lblCreateDate').string
        obj = New.objects.filter(source=source)
        if not obj:
            new = New(title=title, public='jwc', source=source, text=text, type='教务通知', pub_date=pub_date)
            new.save()
            times += 1
print("已更新"+str(times)+"条教务通知。")
