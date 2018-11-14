from django.shortcuts import render
from django.shortcuts import HttpResponse


# Create your views here.
def index(request):
    context = {'title': "ss", 'p': 11}
    return render(request, index, context)
