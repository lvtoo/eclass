"""
Version: 0.1
Author: lvtoo
e-mail: o@oouul.com
Date: 2018/11/25

"""
import requests
from bs4 import BeautifulSoup
from home.models import New
from datetime import datetime

times = 0
url = 'https://www.shmtu.edu.cn'
r = requests.get(url+'/news')
soup = BeautifulSoup(r.content, 'lxml')
div_tag = soup.find('div', class_='view-content')
all_li = div_tag.find_all('li')
for li in all_li:
    a = li.find('a')
    title = a.string
    source = url + a['href']
    pub_date = li.find('span', class_='date-display-single')['content'][:10]
    pub_date = datetime.strptime(pub_date, '%Y-%m-%d')
    r = requests.get(source)
    soup = BeautifulSoup(r.content, 'lxml')
    div_tag = soup.find_all('div', class_='content')[4]
    text = div_tag.text[28:]
    describe = text[:70]
    try:
        img_src = div_tag.find('img')['src']
    except TypeError:
        img_src = ''
    obj = New.objects.filter(title=title)
    if not obj:
        new = New(title=title, public='SMU', source=source, text=text, type='news', pub_date=pub_date,
                  describe=describe, img_url=img_src)
        new.save()
        times += 1
print("已更新" + str(times) + "条校园动态。")
