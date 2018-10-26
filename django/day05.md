### 1.重定向
第一种重定向，地址是硬编码
```
return HttpresponseRedirect('/app/all_stu/')
#括号内写页面的路径
```
第二种重定向，使用反向解析reverse(namespace:name)
```
先定义一个命名空间，然后给url添加一个名字属性
url(r'^app/', include('app.urls',namespace='dy'))
#使用命名空间
return HttpResponseRedirect(reverse('dy:all'))
```
### url反向解析
```
<a href="{% url 'dy:edit' stu.id %}">编辑</a>
```
### http无状态协议
访问某个地址
没登录情况 :http://127.0.0.1:8080/index/----->login.html

已登录情况:http://127.0.0.1:8080/index/------>index.html
#### http无状态协议解决办法：cookie + session
#### cookie的运用---登录/注册/登录状态权限验证
#### 1.创建用户user模块

    创建应用命令:python manage.py startapp user
    在setting.py文件中添加应用user,templates中添加 'DIRS': [os.path.join(BASE_DIR,'templates')]
    
#### 2.定义模板:在templates文件夹中定义父模板base.html ,login.html ,register.html ,index.html

1.父模板base.html

    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>
            {% block title %}
            {% endblock %}
        </title>
        {% block extCSS %}
        {% endblock %}

        {% block JS %}
        {% endblock %}
    </head>
    <body>
        {% block content %}
        {% endblock %}
    </body>
    </html>
    
2.register.html 子模板注册页面
```
    {% extends 'base.html' %}

    {% block title %}
        注册
    {% endblock %}
    
    {% block content %}
        <form action="" method="post">
            {{ form.errors.username }}
            <p>姓名:<input type="text" name="name"></p>
            {{ form.errors.password }}
            <p>密码:<input type="password" name="pw"></p>
            {{ form.errors.password2 }}
            <p>确认密码:<input type="password" name="pw2"></p>
            <input type="submit" value="提交">
    
        </form>
    {{ msg }}
    {% endblock %}
```    
3.login.html 子模板登录界面
```
{% extends 'base.html' %}

{% block title %}
    登录
{% endblock %}

{% block content %}
    <form action="" method="post">
        {{ form.errors.username }}
        <p>姓名:<input type="text" name="name"></p>
        {{ form.errors.password }}
        <p>密码:<input type="text" name="pw"></p>
        <input type="submit" value="提交">
    </form>
{{ msg }}
{% endblock %}
```
4.index.html 首页
```
{% extends 'base.html' %}

{% block title %}
    首页
{% endblock %}

{% block content %}
    <p>我是首页，我需要登录后才能访问</p>
    <a href="{% url 'user:logout' %}">注销</a>
{% endblock %}
```
#### 3.定义路由  
项目文件夹下的路由
```
from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^user/',include('user.urls',namespace='user'))
]

```
应用下的路由
```
from django.conf.urls import url
from user import views
urlpatterns=[
    #注册
    url(r'^register/',views.register,name='register'),
    #登录
    url(r'^login/',views.login,name='login'),
    #首页
    url(r'^index/',views.index,name='index'),
    #注销
    url(r'^logout/',views.logout,name='logout')

]
```
#### 4.views文件下表单的校验
##### 1.导入所需要用到的库
```
#先写编译器自带的库，然后写第三方库，最后写自己定义的库
import random

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from user.models import UserToken
from utils.functions import login_required

from user.models import User
```
##### 2.用户注册的校验

2.1获取参数
```
def register(request):
    if request.method == 'GET':
        return render(request,'register.html')

    if request.method == 'POST':
        #用于创建用户
        #1.获取参数
        name = request.POST.get('name')
        password = request.POST.get('pw')
        password2 = request.POST.get('pw2')
```
2.2校验参数是否完整
```
if not all([name,password,password2]):
    msg = "请填写完整的参数"
    return render(request,'register.html',{'msg':msg})
```
2.3先判断数据库中是否存在该name用户
```
if User.objects.filter(name=name).first():
    msg = "该账号已注册，请登录"
    return render(request, 'register.html', {'msg': msg})
```
2.4校验密码是否一致
```
if password != password2:
    msg = "密码不一致，请重新输入"
    return render(request,'register.html',{'msg':msg})
```
2.5注册
```
User.objects.create(name=name,password=password)
return HttpResponseRedirect(reverse('user:index'))
```
##### 3登录校验
```
def login(request):
    if request.method == 'GET':
        return render(request,'login.html')

    if request.method == 'POST':
```
3.1获取参数
```
name = request.POST.get('name')
password = request.POST.get('pw')
```
3.2验证数据完整性
```
if not all([name,password]):
    msg = '请填写完整的登录信息'
    return render(request,'login.html',{'msg':msg})
```
3.3验证用户是否注册
```
user = User.objects.filter(name=name).first()
    if not user:
    msg = '该账号没有注册，请先注册'
    return render(request,'login.html',{'msg':msg})
```
3.4校验密码
```
if password != user.password:
    msg = '密码不正确'
    return render(request, 'login.html', {'msg': msg})
```
## 重点

### 请求与响应:请求是从浏览器发送请求的时候，传递给后端的
### 响应:后端返回给浏览器的
```
res = HttpResponseRedirect(reverse('user:index'))
#set_cookie(key,value,max_age)
token = ''
s = '1234567890qwertyuioplkjhgfdsazxcvbnm'
for i in range(25):
    token += random.choice(s)
res.set_cookie('token',token,max_age=6000)

#存token值
user_token = UserToken.objects.filter(user=user).first()
if not user_token:
    UserToken.objects.create(token=token,user=user)
else:
    user_token.token = token
    user_token.save()


return res
```
##### 4.装饰器

定义登录验证的装饰器

闭包三个条件:

1.外层函数套内层函数

2.内层函数调外层函数的参数
 
3.外层函数返回内层函数
```
from django.http import HttpResponseRedirect
from django.urls import reverse

from user.models import UserToken


def login_required(func):

    def check_login(request):
        #func是被login_required装饰的函数
        token = request.COOKIES.get('token')
        if not token:
            #cookie中没有登录的标识符，跳转到登录页面
            return HttpResponseRedirect(reverse('user:login'))
        user_token = UserToken.objects.filter(token=token).first()

        if not user_token:
            #token标识符有误，跳转到登录页面
            return HttpResponseRedirect(reverse('user:login'))
        return func(request)

    return check_login
```
##### 首页和注销页面用到了装饰器
```
from utils.functions import login_required
```
##### 5.首页
```
@login_required
def index(request):
    if request.method == 'GET':
        return render(request,'index.html')
```
##### 6.注销页面
```
@login_required
def logout(request):
    if request.method == 'GET':
        #1.删除浏览器cookie中的token参数
        res = HttpResponseRedirect(reverse('user:login'))
        res.delete_cookie('token')

        #2.删除UserToken中的数据
        token = request.COOKIES.get('token')
        UserToken.objects.filter(token=token).delete()
        return res
```

