# -*- coding:utf-8 -*-
# author: SM0558
# datetime: 2021/5/17 17:06
# software: PyCharm
from django import forms
from captcha.fields import CaptchaField
from .models import User


class UserForm(forms.Form):
    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    captcha = CaptchaField(label='验证码')


class RegisterForm(forms.Form):
    gender = (
        ('male', "男"),
        ('female', "女"),
    )
    username = forms.CharField(required=True, error_messages={'required': '邮箱不能为空！'}, label="用户名", max_length=128,
                               min_length=6, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(required=True, error_messages={'required': '密码不能为空！'}, label="密码", max_length=256,
                                min_length=6, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(required=True, error_messages={'required': '确认密码不能为空！'}, label="确认密码", max_length=256,
                                min_length=6, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, error_messages={'required': '邮箱不能为空！'}, label="邮箱地址",
                             widget=forms.EmailInput(attrs={'class': 'form-control'}))
    sex = forms.ChoiceField(label='性别', choices=gender)
    captcha = CaptchaField(required=True, error_messages={'required': '验证码不能为空！'}, label='验证码')
