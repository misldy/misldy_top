from django.shortcuts import render, redirect
from .models import User
from django.views import generic
import hashlib

from .forms import UserForm, RegisterForm


# Create your views here.
class IndexView(generic.ListView):
    template_name = 'ylogin/index.html'

    def get_queryset(self):
        return


class LoginView(generic.FormView):
    model = User
    template_name = 'ylogin/login.html'
    form_class = UserForm

    def get(self, request, *args, **kwargs):
        if request.session.get('is_login', None):
            return redirect("/")
        else:
            login_form = self.form_class()
            return render(request, self.template_name, locals())

    def post(self, request, *args, **kwargs):
        login_form = self.form_class(request.POST)
        message = "请检查填写的内容！"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = User.objects.get(name=username)
            except:
                message = "用户名不存在！"
            else:
                if user.password == hash_code(password):
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.name
                    return redirect('/')
                else:
                    message = "密码不正确！"
        return render(request, self.template_name, locals())


class RegisterView(generic.CreateView):
    model = User
    template_name = 'ylogin/register.html'
    form_class = RegisterForm

    def get(self, request, *args, **kwargs):
        if request.session.get('is_login', None):
            return redirect("/")
        else:
            register_form = self.form_class()
            return render(request, self.template_name, locals())

    def post(self, request, *args, **kwargs):
        register_form = self.form_class(request.POST)
        message = "请检查填写的内容！"
        if register_form.is_valid():  # 获取数据
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            email = register_form.cleaned_data['email']
            sex = register_form.cleaned_data['sex']
            if password1 != password2:  # 判断两次密码是否相同
                message = "两次输入的密码不同！"
            else:
                same_name_user = User.objects.filter(name=username)
                same_email_user = User.objects.filter(email=email)
                if same_name_user:  # 用户名唯一
                    message = '用户已经存在，请重新选择用户名！'
                elif same_email_user:  # 邮箱地址唯一
                    message = '该邮箱地址已被注册，请使用别的邮箱！'
                else:
                    # 当一切都OK的情况下，创建新用户
                    new_user = User.objects.create()
                    new_user.name = username
                    new_user.password = hash_code(password1)
                    new_user.email = email
                    new_user.sex = sex
                    new_user.save()
                    return redirect('/login/')  # 自动跳转到登录页面
        return render(request, self.template_name, locals())


# 注销
def logout(request):
    print(request.POST.get('next_href'))
    if not request.session.get('is_login', None):
        return redirect('/')

    request.session.flush()

    return redirect('/')


def hash_code(s, salt='mysite_login'):
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())  # update方法只接收bytes类型
    return h.hexdigest()
