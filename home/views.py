from django.views.generic import ListView
from home.models import New
from django.views.generic import View
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse, JsonResponse
from django.core import serializers


class Index(ListView):
    model = New
    template_name = 'home/index.html'
    paginate_by = 10
    context_object_name = 'items'
    ordering = ['-pub_date']

    def get_queryset(self):
        return New.objects.filter(display=True)


class IndexApi(ListView):
    ordering = ['-pub_date']
    model = New
    template_name = 'home/ajax.html'
    paginate_by = 5
    context_object_name = 'items'
    page_kwarg = 'p'

    def get_queryset(self):
        return New.objects.filter(display=True)

#
# class SearchApi(ListView, View):
#     model = New
#     template_name = 'home/index.html'
#     paginate_by = 10
#     context_object_name = 'items'
#     ordering = ['-pub_date']


def search_new(request, search_key):
    news = New.objects.filter(title__icontains=search_key).filter(display=True)

    if 1 == len(news):
        # news = news[0]
        # context = {
        #     "title": news.title,
        #     "text": news.text,
        #     "type": news.type,
        #     "pub_date": news.pub_date,
        #     "img_url": news.img_url
        # }
        return HttpResponseRedirect('/detail/' + str(news[0].id))
        # return render(request, 'home/detail.html', context=context)
    else:
        return render(request, 'home/index.html', context={'items': news})


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
        news.view_page += 1
        news.save()
        context = {
            "title": news.title,
            "text": news.text,
            "type": news.type,
            "pub_date": news.pub_date,
            "img_url": news.img_url
        }
        return render(request, 'home/detail.html', context=context)
