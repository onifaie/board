# _from django.contrib.auth.signals import user_logged_in
from django.db import models
from django.contrib.auth.models import User
from django.db.models import Count

class board(models.Model):
    board=models.CharField(max_length=100)
    describtion=models.TextField(max_length=4000)
    # create_by=models.DateField(User)
    create_dt=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.board

    def get_total_topic(self):
        print(post.objects.filter(topic__topboard=self).count())
       
        return  post.objects.filter(topic__topboard=self).count()


    def get_last_topic(self):
        print( post.objects.filter(topic__topboard=self).order_by('-create_dt').first())
       
        return  post.objects.filter(topic__topboard=self).order_by('-create_dt').first()


  

        # return post.objects.filter(board=self).count()


    
    # Create your models here.

class topic(models.Model):
    topboard=models.ForeignKey(board,related_name='topics',on_delete=models.CASCADE)
    toptitle=models.CharField(max_length=100)
    topdis=models.TextField(max_length=4000)
    topcreated_by=models.ForeignKey(User,related_name='topics',on_delete=models.CASCADE)
    topdate_add=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return '{}'.format(self.topboard)

  
    
class post(models.Model):
    message=models.TextField(max_length=4000)
    topic=models.ForeignKey(topic,related_name='topics',on_delete=models.CASCADE)
    create_by=models.ForeignKey(User,related_name='topic',on_delete=models.CASCADE)
    create_dt=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}'.format(self.message)

    