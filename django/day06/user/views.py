from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib import auth

from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import UserRegisterForm,UserLoginForm
def register(request):
    if request.method == 'GET':
        return render(request,'register.html')

    if request.method == 'POST':
        data = request.POST
        # form = UserForm(request.POST)
        #校验form表单传递的参数
        form = UserRegisterForm(data)
        if form.is_valid():
            User.objects.create_user(username=form.cleaned_data.get('username'),
                                     password=form.cleaned_data.get('password'))
            return HttpResponseRedirect(reverse('user:login'))

        else:

            return render(request,'register.html',{'errors':form.errors})

def login(request):
    if request.method == 'GET':
        return render(request,'login.html')

    if request.method == 'POST':
        data = request.POST
        form = UserLoginForm(data)
        if form.is_valid():
            #使用随机标识符也叫签名token
            user = auth.authenticate(username=form.cleaned_data.get('username'),
                              password=form.cleaned_data.get('password'))

            if user:
                #登录,向request.user属性赋值，赋值为登录系统的用户对象
                #1.向页面的cookie中设置sessionid值,(标识符)
                #2.向django_session表中设置对应的标识符
                auth.login(request,user)
                return HttpResponseRedirect(reverse('user:index'))
            else:
                return render(request,'login.html',{'msg':'密码错误'})

        else:
            return render(request,'login.html',{'errors':form.errors})

@login_required
def index(request):
    if request.method == 'GET':
        return render(request,'index.html')

@login_required()
def logout(request):
    if request.method == 'GET':
        auth.logout(request)
        return HttpResponseRedirect(reverse('user:login'))




