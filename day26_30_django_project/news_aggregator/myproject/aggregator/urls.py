# aggregator/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('gather_feed/', views.gather_feed)
]