from django.contrib.auth.signals import user_logged_in
from django.db import models
# from django.contrib.auth import User


class board(models.Model):
    board=models.CharField(max_length=100)
    describtion=models.TextField(max_length=4000)
    # create_by=models.DateField(User)
    create_dt=models.DateTimeField(auto_now_add=True)

def __str__(self):
    return self.board
    # Create your models here.
