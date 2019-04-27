import requests
from bs4 import BeautifulSoup
from datetime import datetime
from home.models import New

url = 'http://www.shmtu.edu.cn'
r = requests.get(url + '/news')  # 获取校园动态网页代码
soup = BeautifulSoup(r.content, 'lxml')  # 用lxml进行解析
div_tag = soup.find('div', class_='view-content')  # 找出指定class类型的div标签
all_li = div_tag.find_all('li')  # 找出li标签，为列表格式
times = 0  # 计数器
for li in all_li:  # 逐一分析
    a = li.find('a')  # 找出a标签
    title = a.string  # 获取链接及标题名
    source = url + a['href']  # 具体动态内容网址
    s = li.find('span', class_='date-display-single')  # 找出指定class类型span标签
    pub_date = s['content'][:10]  # 公布时间为s的content属性前10位
    pub_date = datetime.strptime(pub_date, "%Y-%m-%d")  # 转格式
    r = requests.get(source)  # 获取动态内容网页
    soup = BeautifulSoup(r.content, 'lxml')
    div_tag = soup.find('div', class_='region region-content')
    text = div_tag.text  # text为div块内文本
    describe = text[:70]  # describe为text前70位
    try:  # 尝试寻找动态来源，没有的话保存空字符
        img_src = div_tag.find('img')['src']
    except TypeError:
        img_src = ''
    obj = New.objects.filter(title=title)  # 过滤标题
    if not obj:  # 如果数据库中没有则保存
        new = New(title=title, describe=describe, text=text, type='new', public='SMU', pub_date=pub_date, source=source,
                  img_url=img_src)
        new.save()
        times += 1
    # print(title,describe,source)#试验
print('更新数' + str(times) + '校园动态')  # 显示更新条数
