from django.urls import path
from . import views
# 어떤 주소로 요청이 들어오면, 요청에 대한 뷰를 맵핑하는 속성명이 바로 urlpatterns
urlpatterns =[
    path('', views.index, name='index'),
    path('todo/create/', views.todo_create, name='todo_create'),
]