from flask import Blueprint, request, render_template, session,\
    url_for,redirect
from app.models import db
from utils.function import check

blue = Blueprint('user',__name__)

@blue.route('/')
def hello():
    return 'Hello World'

@blue.route('/login/',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    if request.method == 'POST':
        #获取参数
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'wang' and password == 'qwert123':
            #模拟校验用户名和密码成功，则向session中存储登录成功后的用户id值
            session['user_id'] = 1
            #return redirect(url_for('user.index'))
            return redirect('/app/index/')
        else:
            return render_template('login.html')





@blue.route('/index/')
@check
def index():
    user_id = session['user_id']
    return '这是首页,我的用户id为%s' % user_id


@blue.route('/temp/')
def temp():
    content = ['Python','Flask','Django','Tornado','Sanic']
    content_h2 = '<h2>这是个h2标题</h2>'
    content_h22 = '     <h2>这是h22标题</h2>     '
    return render_template('temp.html',title='模板语法',
                           content=content,content_h2=content_h2,
                           content_h22=content_h22)

@blue.route('/create_db/')
def create_db():
    #第一次迁移模型
    db.create_all()
    return '创建模型成功'

# @blue.route('/drop_db/')
# def drop_db():
#     db.drop_all()
#     return '删除模型成功'