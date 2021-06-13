from django.contrib import admin
from django.contrib.admin.decorators import display
from .models import *
from datetime import datetime

@admin.register(Board)
# Register your models here.
class boardadmin(admin.ModelAdmin):
    list_display=['board','describtion']
    search_fields=['board','describtion']
    list_filter=['board']
    list_display_links=['board']

@admin.register(Topic)
class admintopic(admin.ModelAdmin):
    list_display=['toptitle','topboard','id']
    list_display_links=['toptitle']
    search_fields=['toptitle','topboard']

@admin.register(Post)
class adminpost(admin.ModelAdmin):
    list_display=['topic','create_dt','id']
    # list_display_links=['toptitle']
    search_fields=['message']

    