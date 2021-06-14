from django import forms
from django.forms.widgets import Textarea

from . models import Board, Topic,Post




class BoardFlorm(forms.ModelForm):
    class Meta:
        model=Board
        fields='__all__'


class TopicForm(forms.ModelForm):


    msg=forms.CharField(widget=forms.Textarea,max_length=4000)

    class Meta:
        model=Topic
        fields='__all__'
        # fields=['toptitle','msg']
        exclude=['topcreated_by','topboard']
        
      

# class PostForm(forms.ModelForm):

    # class Meta:

    #     model=Post
    #     fields=['topic','msg']
    #     exclude=('create_by',)
        
      