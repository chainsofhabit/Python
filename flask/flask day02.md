## session 和cookie
###  1.flask中session的两种存储方式

方法1.使用flask默认的方式存储session，其实就是讲session中的数据保存在客户端的cookie中

登录验证：

视图文件
```
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
```
中间件：function.py文件
```
from flask import url_for, session,redirect


def check(func):
    def check_login():

        try:
            session['user_id']
        except Exception as e:
            return redirect(url_for('user.login'))

        return func()

    return check_login
```
manage.py文件
```
app = Flask(__name__)

app.register_blueprint(blueprint=blue,url_prefix='/app')

#设置加密的复杂程度
app.secret_key = 'qwertyuioplkj'
```
初始化flask对象app(两种方法)
```
#第一种
Session(app)
#第二种
sess = Session()
sess.init_app(app)
```

方法2.在服务端中保存session数据，使用flask-session库，配置使用redis进行数据存储

配置session存储数据库
```
app.config['SESSION_TYPE'] = 'redis'
app.config['SESSION_REDIS'] = redis.Redis(host='127.0.0.1',port=6379)

```
数据库配置
```
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@127.0.0.1:3306/flask6'
app.config['SQLALCHEMY_TRACKMODIFICATIONS'] = False

```
初始化app和db
```
db.init_app(app)
```
### 2.模板
1.继承，block块

    {% extends 'xxx.html' %}
    {% block xxx %} {% endblock %}

2.继承block中已填有的内容

    {% block xxx %}
        {{ super() }}
    {% endblock %}

3.标签{% 标签 %}
    
    if,for,block,url_for

4.变量{{ 变量 }}
```
loop.index
loop.index0
loop.revindex
loop.revindex0
loop.first
loop.last

```
5.过滤器
```
upper
lower
safe
length
```
### 3.模型层

使用flask-sqlalchemy库

class x (db.Model):

    id = db.Column(db.Integer,primary_key=True)
    
    约束：unique,nullable,default
    
    表名：__tablename__ = '表名'
    数据路连接格式：mysql+pymysql://root:123456@127.0.0.1:3306/db
    
1.证明模型
```
class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(10),unique=True,
                        nullable=False)
    password = db.Column(db.String(100),nullable=True)
    __tablename__ = 'day02_user'
```
2.创建模型
```
@blue.route('/create_db/')
def create_db():
    #第一次迁移模型
    db.create_all()
    return '创建模型成功'
```
### templates
function.html声明函数
```

<!--声明函数-->
{% macro hello() %}
    <p>江湖再见</p>
{% endmacro %}

{% macro say(name) %}
    <p>你是猴子搬来的救兵吗，{{ name }}</p>
{% endmacro %}
```
temp.html调用函数
```
{% from 'function.html' import hello %}
{% from 'function.html' import say %}


{{ hello() }}
{{ say('江秀成') }}
```