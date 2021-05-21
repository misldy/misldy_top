# -*- coding:utf-8 -*-
# author: SM0558
# datetime: 2021/4/26 15:23
# software: PyCharm
from django.urls import path

from . import views

app_name = 'ylogin'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('logout/', views.logout, name='logout'),
]
