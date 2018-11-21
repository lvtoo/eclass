from django.shortcuts import render
from home.models import New
import json


# Create your views here.
def index(request):
    content = {}
    new = New.objects.filter(display=True).values('title', 'describe', 'pub_date')[0:10]
    for i in range(0, len(new)):
        content.update({i: new[i]})
    return render(request, 'home/index.html', content, status=200)
