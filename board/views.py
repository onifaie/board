from django.shortcuts import render,get_list_or_404,get_object_or_404
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
        # mytopic=topic.objects.filter(topic=id)
        # mytopic= topic.objects.filter(topboard=id)

        mytopic= topic.objects.filter(topboard=id)
        print(board)
      
        return render(request,'topic.html',{'mytopic':mytopic})
        

def postt(request,id):

    mypost=post.objects.filter(topic=id)
    print(mypost)
    return render(request,'post.html',{'mypost':mypost})



  