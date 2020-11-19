from django.views.generic import TemplateView
from . import models
import json
from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import StreamingHttpResponse
from django.template import loader
from PIL import Image

from .models import UserInfo

# 얼굴인식 연결
from home.face_recog import FaceRecog
import os
import numpy

# 지워도 되나
import logging

global face
 


def index(request):
    template = loader.get_template('home/index.html')
    context = {
#         'login_success' : False,
#         'latest_question_list': "test",
    }
    return HttpResponse(template.render(context, request))

def history(request):
    user_point = UserInfo.objects.get(user_id='jisu1105')
    template = loader.get_template('sub/history.html')
    context = {
        "user_point": user_point
#         'login_success' : False,
#         'latest_question_list': "test",
    }
    return HttpResponse(template.render(context, request))  

# 새로운 페이지 생기면 home>urls.py 수정해야함
def popup_chat_home(request):
    template = loader.get_template('home/new_page.html')
    context = {
        'login_success' : False,
        'initMessages' : ["스타필드 코엑스점 채팅 홈페이지에 오신것을 환영합니다",
                          "스타필드 코엑스점 챗봇이 제품, 서비스, 주요기술, 연락처에 대해 답변합니다."]
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
    print(fr.get_name())

def call_cam(request):
    face=FaceRecog()
    return StreamingHttpResponse(gen(face),content_type='multipart/x-mixed-replace; boundary=frame')

def open_img(request):
    red = Image.new('RGB', (500, 500), (255,0,0,0))
    response = HttpResponse(content_type="image/jpeg")
    red.save(response, "JPEG")
    return response



class Custom(TemplateView):
    template_name = "home/custom.html"
    def get_context_data(self, **kwargs):
        context = super(TemplateView, self).get_context_data()
        print("user",self.request.user.username)
        context['username'] = self.request.user.username

        return context

    def post(self, request, **kwargs):
        ins=models.ShareMe()
        data_unicode=request.body.decode('utf-8')
        data=json.loads(data_unicode)
        ins.message=data['message']
        ins.save()

        return HttpResponse('')


class Store(TemplateView):
    template_name = "home/store.html"

    def get_context_data(self, **kwargs):
        context=super(TemplateView, self).get_context_data()
        context['username']=self.request.user.username

        return context

    def post(self, request, **kwargs):
        ins=models.Alarm()
        data_unicode=request.body.decode('utf-8')
        data=json.loads(data_unicode)
        ins.message=data['message']
        ins.save()

        return HttpResponse('')
