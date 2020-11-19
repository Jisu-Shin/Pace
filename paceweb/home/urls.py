from django.contrib import admin
from django.urls import path 
from home import views
 
urlpatterns = [
    path('', views.index, name='index'),
    path('call_pop', views.call_pop, name='call_pop'),
    path('call_cam', views.call_cam, name='call_cam'),
    path('open_img', views.open_img, name='open_img'),
    path('Store', views.Store.as_view()),
    path('Custom', views.Custom.as_view()),
    path('Store/Shistory/', views.Shistory, name='Shistory'),
    path('Custom/Chistory/', views.Chistory, name='Chistory'),
]