# 用户的权限与用户角色
RBAC（Role-Based Access Control，基于角色的访问控制）就是用户通过角色与权限进行关联。简单地说，一个用户拥有若干角色，每一个角色拥有若干权限。这样，就构造成“用户-角色-权限”的授权模型。在这种模型中，用户与角色之间，角色与权限之间，一般都是多对多的关系。

##### 数据库中的表包括用户表，权限表，角色表
##### 思想：1.创建角色；2.角色对应权限；3.用户分配角色；4.（特殊情况）用户分配权限

##### 用户，角色，权限三个表之间的关系都是多对多关系

##### 用户表和权限表之间的ManyToManyFiled()为:user_permissions
##### 用户表和角色表的ManyToManyFiled()为：groups
##### 角色表和权限表的ManyToManyFiled()为：permissions

#### 查询

    #通过用户查询权限
    user.user_permissions.all()
    user.groups.all()[0].permissions.all()

    #django自带查询方法
	user.get_group_permissions()
	user.get_all_permissions()
	
#### 2.权限验证

    #自己实现权限验证
        user.user_permission.filter(codename='xxx')
        user.groups.all()[0].permissions.filter(codename='xxx')
    #django实现权限验证
        user.has_perm('应用名.权限名')

3.装饰器

    #自己实现
    def a(func):
        def b(request):
	return(func(request))
        return b
    #django实现
       @permission_required('应用名.权限名')

### 1.项目文件
1.1 setting文件中修改数据库，添加应用，添加自定义的模型
```
#告诉django,User模型修改为自定义的User模型
AUTH_USER_MODEL = 'user.MyUser'
```
1.2修改路由
```
from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^user/',include('user.urls',namespace='user')),
]
```
### 2.templates文件，存放html文件
2.1login.html(登录)
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <form action="" method="post">
        {% csrf_token %}
        姓名:<input type="text" name="username"><br>
        密码:<input type="text" name="password"><br>
        <input type="submit" value="提交">
    </form>
</body>
</html>
```
2.2 my_index(登录成功)
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <p>登录成功</p>
</body>
</html>
```
2.3permissions查询用户权限
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <!--通过用户查询组，组查询权限-->
    {{ user }}
    {% for permission in user.groups.all.0.permissions.all %}
        {{ permission.codename }}
    {% endfor %}

    <!--通过用户直接查找权限-->
    <br>
    {% for per in user.user_permission.all %}
        {{ per.codename }}
    {% endfor %}

</body>
</html>
```
#### django自带的查询方法
```
def my_index(request):
    if request.method == 'GET':
        # 当前系统登录的用户
        user = request.user
        # 获取当前用户对应组的权限
        user.get_group_permissions()
        # 获取当前用户的所有权限
        user.get_all_permissions()
        # 判断是否有某个权限
        user.has_perm('user.change_my_user_username')

        return render(request,'my_index.html')
```
### 3.应用 user文件
3.1 models文件
```
from django.contrib.auth.models import  AbstractUser
from django.db import models

class MyUser(AbstractUser):
    #扩展django自带的auth_user表，可以自定义新增的字段

    class Meta:
        #django默认给每个模型初始化三个权限
        #默认的是change,delete,add权限
        permissions = (
            ('add_my_user','新增用户权限'),
            ('change_my_user_username','修改用户名权限'),
            ('change_my_user_password','修改用户密码权限'),
            ('all_my_user','查看用户权限')

        )
```
3.2 forms文件，用于登录的表单验证
```
from django import forms

class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=10,min_length=2,
                               required=True,
                               error_messages={
                                   'required':'必填'
                               })

    password = forms.CharField(max_length=20,min_length=3,
                               required=True,
                               error_messages={
                                   'required': '必填'
                               })
```
3.3 urls文件，添加路由
```
from django.conf.urls import url
from user import views
urlpatterns = [
    #创建用户并给用户分配权限
    url(r'^add_user_permission/',views.add_user_permission,name='add_user_permission'),
    #用户名为wangxxx的用户，有查看用户列表权限，才能访问如下的视图函数
    url(r'^index/',views.index,name='index'),
    # 创建组，并分配组权限
    url(r'^add_group_permission/',views.add_group_permission,name='add_group_permission'),
    # 给用户分配审查组
    url(r'^add_user_group/',views.add_user_group,name='add_user_group'),
    # 查看用户权限
    url(r'^show_user_permission/',views.show_user_permission,name='show_user_permission'),
    # 登录
    url(r'^login/',views.login,name='login'),
    url(r'^my_index/',views.my_index,name='my_index'),
    url(r'^new_index/',views.new_index,name='new_index')
]
```
3.4 views文件

导入所需要用到的库
```
from django.contrib import auth
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import Permission, Group
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from user.forms import UserLoginForm
from user.models import MyUser
from utils.functions import check_permissions
```
创建用户，添加权限
```
def add_user_permission(request):
    if request.method == 'GET':
        # 1.创建用户
        user = MyUser.objects.create_user(username='wangxxx',
                                   password='123456')
        # 2.指定刚创建的用户，并分配给它权限（新增用户权限，查看用户权限）
        permissions = Permission.objects.filter(codename__in=['add_my_user','all_my_user']).all()
        for permission in permissions:
            #多对多的添加
            user.user_permissions.add(permission)
        # 3.删除刚创建的用户的新增的权限
        # user.user_permission.remove(权限对象)

    return HttpResponse('创建用户权限成功')
```
自定义装饰器方法查看用户权限
```
def index(request):
    # 用户名为wangxxx的用户，有查看用户列表权限，才能访问如下的视图函数
    #wangxxx用户有查看用户列表权限，才能访问index函数
    #用装饰器写
    if request.method == 'GET':
        return render(request,'index.html')
```
装饰器
```
from django.http import HttpResponse
from django.shortcuts import render

import user
from user.models import MyUser
# 1.外层函数内嵌内层函数
# 2.外层函数返回内层函数
# 3.内层函数调用外层函数的参数

def check_permissions(func):

    def check(request):
        # 用户名为wangxxx的用户，有查看用户列表权限，才能访问如下的视图函数
        user = MyUser.objects.filter(username='wangxxx').first()
        u_p = user.user_permissions.filter(codename='all_my_user').first()
        if u_p:
            #用户有列表权限则继续访问被装饰器装饰的函数
            return func(request)
        else:
            return HttpResponse('用户没有访问权限')
    return check
```
添加组权限
```
def add_group_permission(request):
    if request.method == 'GET':
        # 创建超级管理员(所有权限)，创建普通管理员(修改/查看权限)
        group = Group.objects.create(name='审核组')

        ps = Permission.objects.filter(codename__in=['change_my_user_username',
                                                'change_my_user_password',
                                                'all_my_user']).all()
        for permission in ps:
            group.permissions.add(permission)
        return HttpResponse('创建组权限成功')
```
用户分配组权限
```
def add_user_group(request):
    if request.method == 'GET':
        # 给用户分配审核组
        group = Group.objects.get(name='审核组')
        user = MyUser.objects.get(username='wangxxx')
        # 分配组
        user.groups.add(group)
        return HttpResponse('用户分配组权限成功')
```
显示用户权限
```
def show_user_permission(request):
    if request.method == 'GET':
        user = MyUser.objects.get(username='wangxxx')
        return render(request,'permissions.html',{'user':user})
```
django自带登录验证
```
def login(request):
    if request.method == 'GET':
        return render(request,'login.html')

    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = auth.authenticate(username=form.cleaned_data['username'],
                                     password=form.cleaned_data['password'])
            if user:
                auth.login(request,user)
                return HttpResponseRedirect(reverse('user:my_index'))
            else:
                return render(request,'login.html',{'errors':form.errors})

```