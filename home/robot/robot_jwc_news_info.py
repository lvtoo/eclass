# coding=utf-8
import requests
from bs4 import BeautifulSoup
from home.models import New
from datetime import datetime

# 计数，更新了几条数据
times = 0
# 给jwc一个request
url = "http://jwc.shmtu.edu.cn"
r = requests.get(url + "/jiaowuxinwen")
soup = BeautifulSoup(r.content, 'lxml')
# 获取所有新闻列表的的行
all_news = soup.find('tbody').find_all('tr')

# 每一行分别操作
for new in all_news:
    tds = new.find_all('td')
    # 获得该条信息的超链接
    a = tds[1].find('a', target='_blank')
    if a is not None:
        pub_date = tds[3].get_text()
        pub_date = datetime.strptime(pub_date, '          %Y/%m/%d %H:%M:%S        ')
        source = a['href']
        title = a.get_text()
        source = url + source
        r = requests.get(source)
        soup = BeautifulSoup(r.content, 'lxml')
        div = soup.find('div', class_='field-item')
        all_span = div.find_all('span')
        text = ""
        for span in all_span:
            text += span.get_text()
        text = text[len(title):]
        try:
            img_src = url + div.find('img').get('src')
        except AttributeError:
            img_src = ''
        try:
            describe = text.split('，', 1)[1][:70]
        except IndexError:
            describe = title
        obj = New.objects.filter(title=title)
        if not obj:
            new = New(title=title, public='教务处', source="", text=text, type='news', pub_date=pub_date,
                      describe=describe, img_url=img_src)
            new.save()
            times += 1

print("已更新" + str(times) + "条教务新闻。")
