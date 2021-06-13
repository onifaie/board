from django.urls import path , include

from . import views

# app_name='board'

urlpatterns = [

    path('',views.list_Board,name='list_Board'),
    path('list_Topic/<int:id>/',views.list_Topics,name='list_Topic'),
    # path('New_Topic/<int:id>/new',views.New_Topics,name='New_Topic'),
    path('New_Topic/<int:id>/',views.New_Topics,name='New_Topic'),
   
   
   
   
   
   
   
    # path('list_topic/<int:id>/',views.list_topic, name='list_topic'),
    # path('addnew',views.newaddt, name='addnew'),
    # path('addnewtopic',views.addnewtopicc, name='addnewtopic'),
    # path('addnewboard',views.addnewboard, name='addnewboard'),
    # path('addnewPost/<int:id>/',views.addnewPost, name='addnewPost'),
    # path('DetailsPost/<int:id>/',views.DetailsPost, name='DetailsPost'),

]