# _from django.contrib.auth.signals import user_logged_in
from django.db import models
from django.contrib.auth.models import User
class Board(models.Model):
    board=models.CharField(max_length=100)
    describtion=models.TextField(max_length=4000)
    # topcreated_by=models.ForeignKey(User,related_name='Board_User',on_delete=models.CASCADE,blank=True,default=1)
    create_dt=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.board

    def get_count_post(self):
        # print(post.objects.filter(topic__topboard=self).count())
       
        return  post.objects.filter(topic__topboard=self).count()

    def get_count_tpoic(self):
        # print(post.objects.filter(topic__topboard=self).count())
       
        return  topic.objects.filter(board__board=self).count()


    def get_last_topic(self):
       
        return  Post.objects.filter(topic__topboard=self).order_by('-create_dt').first()


  

        # return post.objects.filter(board=self).count()


    
    # Create your models here.

class Topic(models.Model):
    topboard=models.ForeignKey(Board,related_name='Topic_Board',on_delete=models.CASCADE)
    toptitle=models.CharField(max_length=100)
    topdis=models.TextField(max_length=4000)
    topcreated_by=models.ForeignKey(User,related_name='topics',on_delete=models.CASCADE)
    topdate_add=models.DateTimeField(auto_now_add=True)

    

    def __str__(self):
        return '{}'.format(self.toptitle)

    def get_count_post(self):
        # print(post.objects.filter(topic__topboard=self).count())
       
        return  Post.objects.filter(topic__topic=self).count()


  
    
class Post(models.Model):
    message=models.TextField(max_length=4000)
    topic=models.ForeignKey(Topic,related_name='topics',on_delete=models.CASCADE)
    create_by=models.ForeignKey(User,related_name='topic',on_delete=models.CASCADE)
    create_dt=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return " this topic " + '{}'.format(self.topic)

 


    

    