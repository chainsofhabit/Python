## 1.flask环境
>1.创建虚拟环境
```
virtualenv --no-site-packages flaskenv
```
>2.安装flask
```
pip install flask
```
## 2.flask最小应用
>创建hello.py
```
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'hello'
if __name__ == '__main__':
    app.run()
```
## 3
默认启动命令：python hello.py

默认id和端口：127.0.0.1：5000

## 4.使用flask_script的manage模块
```
from flask import Flask
from flask_script import Manager

app = Flask(__name__)

@app.route('/')
def hello():
    return 'hello'
#使用manage管理app模块
manage = Manage(app)

if __name__ == '__main__':
    manage.run()
```
>启动命令：python hello.py runserver -h IP -p PORT -d
## 5.分离出视图层，业务逻辑，从hello.py 文件中分离出路由和视图函数

**使用蓝图管理路由，蓝图的好处就是模块化管理应用**

创建一个视图views.py文件
```
from flask import Blueprint, url_for, redirect, \
    request,make_response,abort


#第一步，生成蓝图对象，使用蓝图对象管理路由
app_blueprint = Blueprint('app',__name__)

@app_blueprint.route('/hello/',methods=['GET','POST','PATCH'])
def hello_world():
    if request.method == 'GET':
        #获取get请求传递的参数：request.args
        #request.args[key] 或request.args.get(key)或request.args.getlist(key)
        return 'Hello World'
    if request.method == 'POST':
        #TODO：获取POST提交的参数
        #获取POST提交请求传递的参数：request.form
        return '你好，我是POST请求'

#第二步，注册蓝图
app.register_blueprint(blueprint=app_blueprint,url_prefix='/app')
```

## 6.跳转
>url_for('蓝图别名.跳转的函数名')
>redirect(url_for('yyy.xxx'))
```
from flask import Blueprint, url_for, redirect, \
    request,make_response,abort
    
@app_blueprint.route('/redirect/')
def redirect_url():
    #Django写法:HttpResponseRedirect(reverse('name'))
    #Flask写法：redirect(url_for('蓝图名称.跳转的函数'))
    return redirect(url_for('app.hello_world'))
```
## 7.请求与响应
#### request请求
##### 获取get传参：request.args
##### 获取post传参：request.form
##### 获取上传文件：request.files
##### 获取路径：request.path
##### 请求方式：request.method
#### 响应response,是后端产生返回给前端（浏览器）
##### make_response(响应内容，响应状态码(默认为200))
##### 响应绑定cookie,set_cookie/delete_cookie
## 异常的抛出与捕获
>抛出：abort状态码
>捕获：@blue.errorhandler(状态码)
```
@app_blueprint.route('/abort_a/',methods=['POST'])
def abort_a():
    try:
        a = int(request.form.get('a'))
        b = int(request.form.get('b'))
        c = a/b
        return '%s/%s=%s' % (a, b, c)
    except Exception as e:
        #异常抛出
        abort(500)

@app_blueprint.errorhandler(500)
def error_handler(error):
    return 'Exception is %s' % error
```
## 9.路由规则
#### 路由匹配规则
##### <选择器：参数名>
##### 选择器没有int：表示接收的参数为int类型
##### 没有定义选择器：表示接收的参数为string类型(默认)
##### 选择器string：表示接收的参数一定为string类型
##### 选择器：uuid/float/path