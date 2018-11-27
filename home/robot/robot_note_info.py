from pyquery import PyQuery as pq
from home.models import New
from datetime import datetime
import re

times=0
doc = pq("https://www.shmtu.edu.cn/events")
tbody = doc("tbody")
tr = tbody("tr").items()
for i in tr:
    temp = pq(i)
    i_url = temp("a").attr("href")
    lec_urls="https://www.shmtu.edu.cn/"+i_url
    i_time = temp(".date").text().split(',', 1)[0]
    i_time = datetime.strptime(i_time, '%Y-%m-%d')
    i_title = temp(".title").text()
    i_department = temp(".department").text()
    doc = pq(lec_urls)
    title=doc(".title").text()
    cont = doc(".field-item")
    items = cont.children()
    text = ""
    for i in items:
        i = pq(i)
        if (i.is_("table")):
            table = i.outerHtml()
            table = re.sub('<table\s.*?>', '<table>', table)
            table = re.sub('<p\s.*?>', '<p>', table)
            table = re.sub('<tr\s.*?>', '<tr>', table)
            table = re.sub('<td\s.*?>', '<td>', table)
            table = pq(table).addClass("table")
            text = text + str(table)
        else:
            text = text + i.text() + '\n\n'
    i_describe = text[:70]
    obj = New.objects.filter(title=title)
    if not obj:
        new = New(title=i_title, public=i_department, source=lec_urls, text=text, type='notices', pub_date=i_time,
                  describe=i_describe,img_url="")
        new.save()
        times += 1
print("已更新"+str(times)+"条讲座通知。")
# table = cont("table").removeAttr("style").remove()
#