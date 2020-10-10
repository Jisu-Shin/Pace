from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404, HttpResponseNotFound
from django.template import loader

# 얼굴인식 연결
from home.PaceFramework.Pace.face_recog import FaceRecog
import os

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

# 새로운 페이지 생기면 home>urls.py 수정해야함
def popup_chat_home(request):
    template = loader.get_template('home/new_page.html')
    context = {
        'login_success' : False,
        'initMessages' : ["스타필드 코엑스점 채팅 홈페이지에 오신것을 환영합니다",
                          "스타필드 코엑스점 챗봇이 제품, 서비스, 주요기술, 연락처에 대해 답변합니다."]
    }
    return HttpResponse(template.render(context, request))

def call_chatbot(request):
    if request.method == 'POST':
        if request.is_ajax():
            userID = request.POST['user']
            sentence = request.POST['message']
            logger.debug("question[{}]".format(sentence))
            answer = bot.get_answer(sentence, userID)
            # answer = sentence
            logger.debug("answer[{}]".format(answer))
            return HttpResponse(answer)
    return ''