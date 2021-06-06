from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth import  user_logged_in

# Create your views here.
from .models import board

def index(request):

    myboard=board.objects.all().order_by('-id')


    context={
        'board':myboard
    }
    return render(request,'index.html',context)


def topic(request,id):
    myboard=board.objects.get(pk=id)

    print(myboard.board)

    context={
        'board':myboard,
       
    }
    return render(request,'topic.html',context)
