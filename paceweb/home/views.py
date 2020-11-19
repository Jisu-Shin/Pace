from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import StreamingHttpResponse
from django.http import Http404, HttpResponseNotFound
from django.template import loader

from .models import UserInfo

# 얼굴인식 연결
from home.PaceFramework.Pace.face_recog import FaceRecog
import os
import numpy

# 지워도 되나
import logging

face = FaceRecog()
 
def error(request):
    #return HttpResponseNotFound('<h1>not found</h1>')
    raise Http404("Not Found")

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

def call_cam(request):
    g = gen(face)
    try:
        return StreamingHttpResponse(g,content_type='multipart/x-mixed-replace; boundary=frame')
    except:
        pass
