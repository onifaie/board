from django.contrib import admin
from django.contrib.admin.decorators import display
from .models import *
from datetime import datetime

@admin.register(board)
# Register your models here.
class boardadmin(admin.ModelAdmin):
    date=datetime.date
    list_display=['board','describtion']
    search_fields=['board','describtion']
    list_filter=['board']
    list_display_links=['board']