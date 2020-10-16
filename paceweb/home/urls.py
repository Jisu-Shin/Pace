from django.urls import path 
from home import views
 
urlpatterns = [
    path('', views.index, name='index'),
    path('call_pop', views.call_pop, name='call_pop'),
    path('call_cam', views.call_cam, name='call_cam'),
]