import requests
from bs4 import BeautifulSoup

r = requests.get("http://jwc.shmtu.edu.cn/")
soup = BeautifulSoup(r.text, 'lxml')
# find = soup.find('p')
# print(type(find), find, find.name, find['class'])
all_li = soup.find('div', id='marquee1').find('ul').find_all('li')
for li in all_li:
    a = li.find('a')
    if a is not None:
        print('标题：' + a['title'])
