from django.shortcuts import render,get_list_or_404
from django.http import HttpResponse

from django.contrib.auth import  user_logged_in

# Create your views here.
from .models import board,topic,post
from board import models

def index(request):

    myboard=board.objects.all()
    print(topic.topboard)


    context={
        'board':myboard,
    }
    return render(request,'index.html',context)


def topicc(request,id):
        # mytopic=get_list_or_404(topic,topboard_id=id)
        mytopic=topic.objects.filter(topic=id)

            
        context={
                'mytopic':mytopic,
            
            }
        return render(request,'topic.html',context)
        

       

  