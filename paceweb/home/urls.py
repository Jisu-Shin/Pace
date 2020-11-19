from django.contrib import admin
from django.urls import path 
from home import views
 
urlpatterns = [
    path('', views.index, name='index'),
    path('history/', views.history, name='history'),
    path('call_pop', views.call_pop, name='call_pop'),
    path('call_cam', views.call_cam, name='call_cam'),
]