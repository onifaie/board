from django.urls import path , include

from . import views

urlpatterns = [
    path('',views.index,name='index'),
    # path('Details/<int:board_id>',views.Details,name='Details'),
    path('topic/<int:id>/',views.topicc, name='topic'),
    path('post/<int:id>/',views.postt, name='post'),
    path('DetailsPost/<int:id>/',views.DetailsPostt, name='DetailsPost'),

]