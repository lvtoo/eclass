from django.shortcuts import render
from django.shortcuts import HttpResponse


# Create your views here.
def index(request):
    context = {'code': 200,
               'title': "海大资讯",
               'p': '功能正在开发~敬请期待'}
    return render(request, 'index.html', context)
