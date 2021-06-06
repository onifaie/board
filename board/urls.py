from django.urls import path , include

from . import views

urlpatterns = [
    path('',views.index,name='index'),
    # path('Details/<int:board_id>',views.Details,name='Details'),
    path('topic/<int:id>/',views.topic, name='topic')

]