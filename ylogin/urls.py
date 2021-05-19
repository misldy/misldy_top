# -*- coding:utf-8 -*-
# author: SM0558
# datetime: 2021/4/26 15:23
# software: PyCharm
from  django.urls import path

from . import views

app_name = 'ylogin'

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]