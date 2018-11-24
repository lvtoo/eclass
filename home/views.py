from django.views.generic import ListView
from home.models import New
from django.views.generic import View
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers


class Index(ListView):
    model = New
    template_name = 'home/index.html'
    paginate_by = 10
    context_object_name = 'news'
    ordering = 'pub_date'


class IndexApi(ListView):
    model = New
    template_name = 'home/ajax.html'
    paginate_by = 5
    context_object_name = 'news'
    ordering = 'pub_date'
    page_kwarg = 'p'

# def getdata(request):
#     news = New.objects.order_by('pub_date').values('title', 'describe', 'pub_date', 'type')[a-10:a]
#     if not news:
#         return JsonResponse({'msg': '440'})
#     else:
#         # print(news)
#         # data = serializers.serialize("json",news)
#         news = list(news)
#         a = a + 3
#         print(a)
#         return JsonResponse(news, safe=False)


class NewsDetailView(View):
    def get(self, request, news_id):
        news = New.objects.get(id__exact=news_id)
        context = {
            "title": news.title,
            "text": news.text,
            "type": news.type,
            "pub_date": news.pub_date

        }
        return render(request, 'home/detail.html', context=context)
