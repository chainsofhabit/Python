# Django
## 1.MVC
MVC全名Model View Controller---->模型（model）-视图（view）-控制器（controller）

一种软件设计典范，用一种业务逻辑、数据、界面显示分离的方法组织代码

将业务逻辑聚集到一个部件里面，在改进和个性化定制界面及用户交互的同时不需要重新编写业务逻辑。

Model:数据存取层，用于封装于应用程序的业务逻辑相关的数据，以及对数据的处理

View:表现层，负责数据的显示和呈现，渲染的html页面给用户，或者返回数据给用户

Controller:业务逻辑层负责从用户端收集用户的输入，进行业务逻辑处理，包括向模型中发送数据，进行CRUD操作
## 2.MVT
Django=====>MVT

MVT全名Model View Template

严格来说，Django的模式应该是MVT模式，本质上和MVC没有什么区别，也是各组件之间问了保持耦合关系，只是定义上有些不同

Model:模型层，负责业务与数据库（ORM）的对象

View:视图层，负责业务逻辑并适当调用Model和Template

Template:模板，负责把页面渲染展示给用户

注意:django中还有一个url分发器，也叫做路由，主要用于将url请求发给不同的View处理，View在进行相关的业务逻辑处理

## 3.虚拟环境
隔离环境---创建虚拟环境
### 3.1创建虚拟环境
virtualenv --no-site-packages djenv6
进入虚拟文件夹

--no-site-packages表示创建的虚拟环境是空白的

-p 如果安装了不止一个python版本加 -p 命令 并指定路径
### 虚拟环境里常用的命令
1.查看虚拟环境下安装的所有的包

    pip list 

2.列出虚拟环境中通过pip安装的包

    pip freeze 

3.启动虚拟环境

    activate 

4.退出虚拟环境

    deactive 

5.进入虚拟环境后安装django

    pip install django==1.11

6.查看所有命令

    python manage.py

7.将端口修改为8080（默认是8000）

    python manage.py runserver 8080 -

8.创建项目

django-admin startproject 项目名称day01

    day01工程目录文件夹,__init__.py,setting.py,urls.py,wsgi.py
    manage.py 工程集管理入口

9.访问后台管理

    http://127.0.0.1:8080/admin
    
10.修改数据库配置setting.py

    ENGINE,USER,PASSWORD,HOST,PORT,NAME

11.映射模型到数据库中

    python manage.py migrate

12.安装数据库驱动

    pip install pymysql

13.初始化数据库的驱动__init__.py

    import pymysql
    pymysql.install_as_mysqldb()
    
14.创建超级管理员

    python manage.py createsuperuser

