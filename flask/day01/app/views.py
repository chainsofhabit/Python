import uuid

from flask import Blueprint, url_for, redirect, \
    request,make_response,abort

#第一步，生成蓝图对象，使用蓝图对象管理路由
app_blueprint = Blueprint('app',__name__)

#request请求
#获取get传参：request.args
#获取post传参：request.form
#获取上传文件：request.files
#获取路径：request.path
#请求方式:request.method

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

#路由匹配规则
#<选择器：参数名 >
#选择器有int：表示接收的参数为int类型
#没有定义选择器：表示接收的参数为string类型（默认）
#选择器string：表示接收的参数一定为string类型
#选择器：uuid/float/path

@app_blueprint.route('/student/<int:id>/')
def student(id):
    return '我是学号为%d的学生' % id


@app_blueprint.route('/course/<id>/')
def course(id):
    return '我是id为%s的课程' % id


@app_blueprint.route('/hello/<string:name>/')
def hello_name(name):
    return '你好:%s' % name


@app_blueprint.route('/float/<float:number>/')
def hello_float(number):
    return '我是float类型的参数:%s' % number


@app_blueprint.route('/path/<path:name>/')
def path_name(name):
    return 'path:%s' % name


@app_blueprint.route('/get_uuid/')
def get_uuid():
    uu = uuid.uuid4()
    return str(uu)


@app_blueprint.route('/uuid/<uuid:name>/')
def uuid_name(name):
    return 'uuid:%s' % name

@app_blueprint.route('/redirect/')
def redirect_url():
    #Django写法:HttpResponseRedirect(reverse('name'))
    #Flask写法：redirect(url_for('蓝图名称.跳转的函数'))
    return redirect(url_for('app.hello_world'))


#响应response,是后端产生返回给前端(浏览器)
#make_response(响应内容，响应状态码(默认为200))
#响应绑定cookie,set_cookie/delete_cookie



@app_blueprint.route('/make_response/',methods=['GET'])
def make_my_response():

    res = make_response('<h2>有点累</h2>')

    return res


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
    #TODO：返回错误页面
    return 'Exception is %s' % error
