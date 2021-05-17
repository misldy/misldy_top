from django.shortcuts import render, HttpResponseRedirect, redirect
from .models import User
from django.views import generic

from .forms import UserForm


# Create your views here.
def index(request):
    a = request.session.get('is_login')
    print(a)
    return render(request, 'ylogin/index.html')
# class IndexView(generic.DetailView):
#     template_name = 'ylogin/index.html'

    # def dispatch(self, request, *args, **kwargs):
    #     user = request.session.get('user', False)
    #     context = {'user': user}
    #     return render(request, self.template_name, context)


class RegisterView(generic.DetailView):
    template_name = 'ylogin/register.html'

    def dispatch(self, request, *args, **kwargs):
        user = request.session.get('user', False)
        context = {'user': user}
        return render(request, self.template_name, context)


# 显示页面
def registerView(request):
    user = request.session.get('user', False)
    if not user:
        return render(request, 'ylogin/login.html')
    else:
        return HttpResponseRedirect('/')


# class


# 注册
def register(request):
    check = False
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = User(**form.cleaned_data)
            user.save()
            check = True
            return render(request, 'ylogin/immediate.html', {'check': check})

    return HttpResponseRedirect('/')


# 登录
def login(request):
    message = None
    if request.session.get('is_login', None):
        return redirect('/')

    if request.method == "POST":
        login_form = UserForm(request.POST)
        message = "请检查填写的内容！"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = User.objects.get(name=username)
                if user.password == password:
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.name
                    return redirect('/')
                else:
                    message = "密码不正确！"
            except:
                message = "用户名不存在！"
        return render(request, 'ylogin/login.html', locals())
    login_form = UserForm()
    return render(request, 'ylogin/login.html', locals())


# 注销
def logout(request):
    if not request.session.get('is_login', None):
        return redirect('/')

    request.session.flush()

    return redirect('/')
