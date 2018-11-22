from django.shortcuts import render
from django.views.generic import ListView
from home.models import New
import json
from django.views.generic import View


# Create your views here.
class newsIndex(ListView):
    model = New
    template_name = 'home/index.html'
    paginate_by = 10
    context_object_name = 'news'
    ordering = 'pub_date'
