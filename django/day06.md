# 使用django自带的auth模块实现注册登录验证
django自带一个app auth模块，在使用auth模块实现登录注册的验证的是后我们就不用写models文件，只需要用到views,url,templates等文件，并且不需要我们自己去创建用户表去存储用户的登录名和密码等数据，在新建数据库的时候auth模块会帮我们创建
## templates模块
#### 1.base
index.html,login.html,register.html文件都是继承于base.html文件
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>
        {% block title %}
        {% endblock %}
    </title>
</head>
<body>
    {% block content %}
    {% endblock %}
</body>
</html>
```

#### 2.register
注册界面,用户名，密码等都限制了长度，如果输入有误会有提示信息
```
{% extends 'base.html' %}

{% block title %}
    注册
{% endblock %}

{% block content %}
    <form action="" method="post">


        <p>姓名:<input type="text" name="username"></p>
        <p>密码:<input type="password" name="password"></p>
        <p>确认密码:<input type="password" name="password2"></p>
        <input type="submit" value="提交">

    </form>
    {% if errors.username %}
        姓名错误信息:{{ errors.name }}
    {% endif %}

    {% if errors.password %}
        密码错误信息:{{ errors.password }}
    {% endif %}

    {% if errors.passeord2 %}
        确认密码错误信息:{{ errors.password2 }}
    {% endif %}
{% endblock %}
```

#### 3.login
登录界面
```
{% extends 'base.html' %}

{% block title %}
    登录
{% endblock %}

{% block content %}
    <form action="" method="post">

        <p>姓名:<input type="text" name="username"></p>

        <p>密码:<input type="password" name="password"></p>
        <input type="submit" value="提交">
    </form>
    {% if errors.username %}
        姓名错误: {{ errors.username }}
    {% endif %}
    {% if errors.password %}
        密码错误: {{ errors.password }}
    {% endif %}
{% endblock %}
```
#### 4.index
首页，登录成功后显示的页面
```
{% extends 'base.html' %}

{% block title %}
    首页
{% endblock %}

{% block content %}
    <p>我是首页，我需要登录后才能访问</p>
{% endblock %}
```
## user模块
### forms表单
1.导入所需要用到的包
```
from django import forms
from django.contrib.auth.models import User

```
2.定义一个用户注册的表单
包括注册时的用户名，密码以及在此确认密码

error_messages用于显示输入时的错误信息
```
class UserRegisterForm(forms.Form):
    username = forms.CharField(max_length=10,min_length=2,
                           required=True,
                           error_messages={
                               'required':'注册姓名必填',
                               'min_length':'账号不能短于两个字符',
                               'max_length':'账号长度不能超过十个字符'
                           })
    password = forms.CharField(max_length=30, required=True,
                         error_messages={
                             'required': '密码必填',
                             'max_length': '密码长度不能超过三十个字符'
                         })

    password2 = forms.CharField(max_length=30, required=True,
                         error_messages={
                             'required': '密码必填',
                             'max_length': '密码长度不能超过三十个字符'
                         })

```
3.验证该用户名是否已经注册，用户两次输入的密码是否一致
```
def clean(self):
    user = User.objects.filter(username=self.cleaned_data.get('username')).first()
    if user:
        raise forms.ValidationError({'username':'账号已注册'})
    if self.cleaned_data.get('password') != self.cleaned_data.get('password2'):
        raise forms.ValidationError({'password':'密码不一致'})
    return self.cleaned_data
```
4.定义一个用户登录的表单，和注册表单类似，只是没有确认密码部分
```
class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=10, min_length=2,
                               required=True,
                               error_messages={
                                   'required': '注册姓名必填',
                                   'min_length': '账号不能短于两个字符',
                                   'max_length': '账号长度不能超过十个字符'
                               })
    password = forms.CharField(max_length=30, required=True,
                               error_messages={
                                   'required': '密码必填',
                                   'max_length': '密码长度不能超过三十个字符'
                               })
```
5.登录时验证该账号是否已经注册
```
def clean(self):
    user = User.objects.filter(username=self.cleaned_data.get('username')).first()
    if not user:
        raise forms.ValidationError({'username':'该账号还没注册，请先注册'})

    return self.cleaned_data
```
### views视图
1.导入包
```
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib import auth

from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import UserRegisterForm,UserLoginForm
```
2.注册
```
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
```
3.登录，向request.user属性赋值，赋值为登录系统的用户对象

3.1向页面的cookie中设置sessionid值(标识符)

3.2向diango_session表中设置对应的标识符

auth自带的login功能,只需要传入user
```
auth.login(request,user)
```

```
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
                auth.login(request,user)
                return HttpResponseRedirect(reverse('user:index'))
            else:
                return render(request,'login.html',{'msg':'密码错误'})

        else:
            return render(request,'login.html',{'errors':form.errors})
```
4.首页（使用登录装饰器）
```
@login_required
def index(request):
    if request.method == 'GET':
        return render(request,'index.html')
```
5.注销（使用装饰器）
```
@login_required()
def logout(request):
    if request.method == 'GET':
        auth.logout(request)
        return HttpResponseRedirect(reverse('user:login'))
```
## utils模块
包括__init__和middleware文件
#### middleware
中间件
1.现在setting文件中添加中间件名称
```
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'utils.middleware.Test1Middleware',
    'utils.middleware.Test2Middleware',
]
```
2.导入包
```
from django.utils.deprecation import MiddlewareMixin
```
3.执行中间件
```
class Test1Middleware(MiddlewareMixin):

    def process_request(self,request):
        print('process_request1')
        #继续执行对应的视图函数
        return None

    def process_response(self,request,response):
        print('process_response1')
        #返回响应
        return response

class Test2Middleware(MiddlewareMixin):

    def process_request(self,request):
        print('process_request2')
        #继续执行对应的视图函数
        return None
```
## 中间件
中间件是一个轻量级的，底层的插件，可以介入Django的请求和响应的过程(面向切面编程)，中间件的本质是一个python类
注意：中间件是帮助我们在视图函数执行之前和执行之后都可以做一些额外的操作，它本质上就是一个自定义类，类中定义了几个方法，Django框架会在请求的特定时间去执行这些方法
#### 每个中间件都是一个独立的类，有以下几个方法
```
1.process_request(self,request)
    执行时机在接收到request之后，但仍未解析出url以确定运行那个视图函数view之前
    
2.process_view(self,request,view_func,view_args,view_kwargs)
    执行时机在django执行完request预处理函数并确定待执行的view之后，但在视图函数view之前
    request: HttpRequest对象
	view_fun: 是django将要调用的视图函数, 是真实的函数对象本身
	view_args: 将传入view的位置参数列表, 不包括request参数
	view_kwargs: 将传入view的字典参数

3. process_response(self, request, response)
	该方法必须返回HttpResponse对象, 可以是原来的, 也可以是修改后的

	调用时机在django执行完view函数并生成response之后, 该中间件能修改response的内容, 常见用途比如压缩内容
	request是request对象
	response是从view中返回的response对象
```