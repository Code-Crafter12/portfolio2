from django.urls import path
from . import views

urlpatterns =[
    path('',views.index, name='index'),
    path('video/',views.video, name='video'),
    path('chat/',views.chat, name='chat'),
    path('carM/',views.carM, name='carM'),
    path('blog1/',views.blog1, name='blog1'),
    path('blog2/',views.blog2, name='blog2'),
    path('blog3/',views.blog3, name='blog3'),
]