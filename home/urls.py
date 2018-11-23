from django.urls import path
from .import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('detail/<news_id>', views.NewsDetailView.as_view(), name='news_detail'),
]
