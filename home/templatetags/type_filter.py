from django import template


register = template.Library()

def type_judge(type):
    if (type == 'news') :
        return "新闻动态"
    else:
        return "通知公告"

register.filter("type_judge",type_judge)