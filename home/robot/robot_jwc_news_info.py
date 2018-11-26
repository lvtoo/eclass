# coding=utf-8
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
all_li = soup.find('div', id='marquee1').find('ul').find_all('li')


for li in all_li:
    a = li.find('a')
    if a is not None:
        source = a['href']
        title = a['title']
        source = url + source
        r = requests.get(source)
        soup = BeautifulSoup(r.content, 'lxml')
        div = soup.find('div', id='content')
        text = div.text
        img_src = 'http://jwc.shmtu.edu.cn' + div.find('img').get('src')
        pub_date = soup.find('span', id='lblCreateDate').string.split(' ', 2)[1]
        pub_date = datetime.strptime(pub_date, '%Y/%m/%d')
        describe = text.split('，', 1)[1][:70]
        obj = New.objects.filter(title=title)
        if not obj:
            new = New(title=title, public='教务处', source=source, text=text, type='news', pub_date=pub_date,
                      describe=describe, img_url=img_src)
            new.save()
            times += 1

        # else:
            # 临时更新数据表
            # obj.describe = text.split('，', 1)[1][:40]
            # obj.pub_data = pub_date
            # obj.save()
            # print(pub_date)

        # new = New.objects.update_or_create(defaults={'title': title},
        #                                    title=title,
        #                                    public='jwc',
        #                                    source=source,
        #                                    text=text,
        #                                    type='教务通知',
        #                                    describe=text[len(title) + 9:len(title) + 9],
        #                                    pub_date=pub_date)
        # if not new:
        #     times += 1

print("已更新" + str(times) + "条教务通知。")

