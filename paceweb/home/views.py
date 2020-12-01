from django.views.generic import TemplateView
from . import models
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.http.response import StreamingHttpResponse
from django.template import loader
from PIL import Image

from .models import *

# 얼굴인식 연결
from home.face_recog import FaceRecog
import os
import numpy

# 지워도 되나
import logging

global face
 
customer_name=None

def index(request):
    template = loader.get_template('home/index.html')
    context = {
#         'login_success' : False,
#         'latest_question_list': "test",
    }
    return HttpResponse(template.render(context, request))

def call_pop(request):

    template = loader.get_template('sub/popup.html')
    context = {
#         'login_success' : False,
#         'latest_question_list': "test",
    }
    return HttpResponse(template.render(context, request))


def gen(fr):
    for i in range(10):
        jpg_bytes = fr.get_jpg_bytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + jpg_bytes + b'\r\n\r\n')       
               
    global customer_name 
    customer_name= fr.get_name()[0]
    

def call_cam(request):
    face=FaceRecog()
    return StreamingHttpResponse(gen(face),content_type='multipart/x-mixed-replace; boundary=frame')

def open_img(request):
    red = Image.new('RGB', (500, 500), (255,0,0,0))
    response = HttpResponse(content_type="image/jpeg")
    red.save(response, "JPEG")
    return response


# def get_name(request):
#     global customer_name 
#     print("get_name: ",customer_name)
#     context= {
#         'customer' : customer_name
#     }
#     return HttpResponse(json.dumps(context),content_type="application/json")



# def history(request):
#     print("history",customer_name)
#     user_point = UserInfo.objects.get(user_id=customer_name)
#     template = loader.get_template('sub/history.html')
#     context = {
#         "user_point": user_point
#     }
#     return HttpResponse(template.render(context))  


def get_name():
    global customer_name
    return customer_name

class Chistory(TemplateView):    
    template_name = "sub/Chistory.html"
    
    def get_context_data(self, **kwargs):
        context = super(TemplateView, self).get_context_data()
        print("user",self.request.user.username)
        name = get_name()
        print("name",name)
        context['username'] = self.request.user.username
        user_point = UserInfo.objects.get(user_id=name)
        context['user_point'] = user_point

        return context

    def post(self, request, **kwargs):
        ins=models.ShareMe()
        data_unicode=request.body.decode('utf-8')
        data=json.loads(data_unicode)
        ins.message=data['message']
        ins.save()

        return HttpResponse('')

class Custom(TemplateView):
    template_name = "home/custom.html"
    @csrf_exempt
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        return JsonResponse({"message": "success"});


class Store(TemplateView):
    template_name = "home/store.html"
    @csrf_exempt
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        message = request.POST['message'];
        point = int(message)
        print(type(point));
        # DB 값 변경 및 변경된 값 화면에 전달
        user = UserInfo.objects.get(user_id="ryeon")
        if user.user_point >= point:
            user.user_point -= point
            user.save()
            message = user.user_point
        else :
            message = "You don't use point"

        return JsonResponse({"message": message});

class Shistory(TemplateView):
    template_name = "sub/Shistory.html"

    @csrf_exempt
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        return JsonResponse({"message": "success"});  
