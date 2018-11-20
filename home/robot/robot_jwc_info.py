# coding=utf-8
import requests
from bs4 import BeautifulSoup
from home.models import News
url = "http://jwc.shmtu.edu.cn/"
r = requests.get(url)
soup = BeautifulSoup(r.content, 'lxml')

# 数据库操作示例
# models.News.objects.create()
all_li = soup.find('div', id='marquee1').find('ul').find_all('li')
for li in all_li:
    a = li.find('a')
    if a is not None:
        new = News(title=a['title'], public='jwc', source=a['href'], text='待获取', type='教务通知')
        new.save()
        # print('标题：' + a['title'])
