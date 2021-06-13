from django.http.response import HttpResponsePermanentRedirect, HttpResponseRedirect
from django.shortcuts import redirect, render,get_list_or_404,get_object_or_404
from django.http import HttpResponse
from .forms import BoardFlorm, TopicForm
from .models import Board,Topic,Post,User

import sys 
sys.setcheckinterval(2010)

def list_Board(request):
    Data=Board.objects.all()
    return render(request,'list_Board.html',{'Data':Data})


def list_Topics(request,id):
   
    board = get_object_or_404(Board,pk=id)
    return render(request,'list_Topic.html',{'board':board})

 
   
    


# def New_Topics(request,id):
#     board = get_object_or_404(Board,pk=id)
#     print(board)
#     user = User.objects.first()
#     form=TopicForm()
#     print(form)
#     if request.method == "POST":

#         form=TopicForm(data=request.post)
        
#         if form.is_valid():
#             topic = form.save(commit=False)
#             topic.topboard=board
#             topic.topcreated_by=user
#             topic.save()
#             post=Post.objects.create(
#                 message=form.cleaned_data.get('msg'),
#                 created_by=user,
#                 topic=topic

#             )
#             print(post)
#             return redirect('list_Topic',id=board.pk)
#     else:
#         print('this form wrong ???????????')
#         form = TopicForm()

#         return render(request,'new_topic.html',{'board':board,'form':form})


def New_Topics(request,id):
    board = get_object_or_404(Board,pk=id)
    print(board.pk)
    user = User.objects.first()
    form =TopicForm()

    if request.method=="POST":
        print(user)

        form =TopicForm(request.POST)
        print(form)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.topboard = board
            topic.topcreated_by = user
            topic.save()

            post = Post.objects.create(
                message=form.cleaned_data.get('msg'),
                create_by = user,
                topic=topic

            )
            return redirect('list_Topic',id=board.pk)
    else:
        form =TopicForm()

    return render(request,'New_Topic.html',{'board':board,'form':form})
