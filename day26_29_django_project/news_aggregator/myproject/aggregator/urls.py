# aggregator/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('gather_feed/', views.gather_feed),
    path('show_articles/', views.show_articles),
    path('show_articles_json/', views.show_articles_json)
]