# -*- coding:utf-8 -*-
# author: SM0558
# datetime: 2021/4/26 15:23
# software: PyCharm
from  django.urls import path

from . import views

app_name = 'ylogin'

urlpatterns = [
    path('', views.index),
    path('registerView/', views.registerView),
    path('register/', views.register),
    path('login/', views.login),
    path('accounts/login/', views.logout),
]