from django.urls import path 
from home import views
 
urlpatterns = [
    path('', views.index, name='index'),
    path('call_pop', views.call_chatbot, name='call_pop'),
]