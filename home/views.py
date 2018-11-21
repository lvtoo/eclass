from django.shortcuts import render


# Create your views here.
def index(request):
    content = {'code': 200,
               'title': "海大资讯",
               'p': '功能正在开发~敬请期待'}
    return render(request, 'home/index.html', content)
