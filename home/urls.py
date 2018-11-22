from django.urls import path
from .import views

urlpatterns = [
    path('', views.newsIndex.as_view(), name='index'),
]
