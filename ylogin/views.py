from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from .models import User
from django import forms
from django.views import generic


class Fuser(forms.Form):
    username = forms.CharField(max_length=50)
    email = forms.CharField(max_length=60)
    password = forms.CharField(max_length=20)



# Create your views here.
# def index(request):
#     user = request.session.get('user', False)
#     return render(request, 'ylogin/index.html', {'user': user})
class IndexView(generic.DetailView):
    template_name = 'ylogin/index.html'

    def dispatch(self, request, *args, **kwargs):
        user = request.session.get('user', False)
        context = {'user': user}
        return render(request, self.template_name, context)

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
        form = Fuser(request.POST)
        if form.is_valid():
            user = User(**form.cleaned_data)
            user.save()
            check = True
            return render(request, 'ylogin/immediate.html', {'check': check})

    return HttpResponseRedirect('/')


# 登录
def login(request):
    user = request.POST['username']
    password = request.POST['password']
    result = User.objects.get(username=user, password=password)

    if not result:
        return HttpResponseRedirect('/registerView/')
    else:
        request.session['user'] = user
        return HttpResponseRedirect('/')


# 注销
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')


