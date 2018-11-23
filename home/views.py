from django.views.generic import ListView
from home.models import New
from django.views.generic import View
from django.shortcuts import render



class Index(ListView):
    model = New
    template_name = 'home/index.html'
    paginate_by = 10
    context_object_name = 'news'
    ordering = 'pub_date'
class NewsDetailView(View):
    def get(self,request,news_id):
        news =New.objects.get(id__exact=news_id)
        context ={
            "title" : news.title,
            "text": news.text,
            "type" : news.type,
            "pub_date" : news.pub_date

        }
        return render(request,'home/detail.html',context=context)
