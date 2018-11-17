## 一对多与多对多关系
#### 学生信息已创建，添加班级和课程信息

1.班级模型
```
class Grade(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    g_name = db.Column(db.String(10),nullable=True,unique=True)
    student = db.relationship('Student',backref='g')


s_c = db.Table('s_c',
               db.Column('s_id',db.Integer,db.ForeignKey('student.id')),
               db.Column('c_id',db.Integer,db.ForeignKey('course.id')),
            )
```
课程模型
```
class Course(db.Model):

    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    c_name = db.Column(db.String(10),nullable=False,unique=True)
    student = db.relationship('Student',secondary=s_c,backref='cou')

    __tablename__ = 'course'
```
2.添加班级信息
```
@blue.route('/add_grade/',methods=['POST'])
def add_grade():
    grades = ['大一','大二','大三','大四']
    g_list = []
    for i in grades:
        g = Grade()
        g.g_name = i
        # db.session.add(g)
        g_list.append(g)
    db.session.add_all(g_list)
    db.session.commit()
```
添加课程信息
```
@blue.route('/add_course/', methods=['POST'])
def add_course():
    cou = Course()
    cou.c_name = '大学英语'
    db.session.add(cou)
    db.session.commit()
```
3.添加学生的课程信息
```
@blue.route('/cous/<int:id>',methods=['GET','POST'])
def cous(id):
    if request.method == 'GET':
        cous = Course.query.all()
        return render_template('cous.html',cous=cous)

    if request.method == 'POST':
        # 向中间表s_c中加入数据
        cou_id = request.form.get('cou.id')
        s_id = id
        # 获取对象
        stu = Student.query.get(s_id)
        cou = Course.query.get(cou_id)
        #关系指定
        stu.cou.append(cou)
        # cou.student.append(stu)
        db.session.commit()

        return redirect(url_for('app.all_stu'))
```
删除学生的课程
```
@blue.route('/del_stu_cou/<int:id>/',methods=['GET','DELETE'])
def del_stu_cou(id):
    if request.method == 'GET':
        stu = Student.query.get(id)
        cous = stu.cou
        return render_template('s_c.html',cous=cous,s_id=id)

    if request.method == 'DELETE':
        c_id = request.form.get('c_id')
        s_id = request.form.get('s_id')
        #获取对象
        stu = Student.query.get(s_id)
        cou = Course.query.get(c_id)
        #删除学生和课程的关联关系
        stu.cou.remove(cou)
        db.session.commit()
        return jsonify({'code':200,'msg':'请求成功'})
```
### django中的中间件

##### process_request
##### peocess_view
##### process_template_response
##### process_exception
##### process_response

### 钩子函数
```
@blue.before_request
def before_request():
    print('before_request')


@blue.before_request
def before1_request():
    print('before1_request')


@blue.after_request
def after_request(response):
    print('after_request')
    return response


@blue.teardown_request
def teardown_request(exception):
    print('teardown_request')
```

4.删除学生课程页面
```

{% extends 'base.html' %}


{% block js %}
    <script src="https://code.jquery.com/jquery-3.1.1.min.js"></script>
    <script>
        function del_cou(c_id,s_id){
            $.ajax({
                url: '/app/del_stu_cou/' + s_id + '/',
                dataType:'json',
                type:'DELETE',
                data:{'c_id':c_id,'s_id':s_id},
                success:function(data){
                    if(data.code == '200'){
                        location.href='/app/all_stu/'
                    }
                },
                error:function(data){
                    alert('删除失败')
                }
            })
        }
    </script>

{% endblock %}

{% block content %}
    {% for c in cous %}
        <p>
            {{ c.c_name }}
            <a onclick="del_cou({{ c.id }},{{ s_id }})">删除</a>
        </p>
    {% endfor %}
{% endblock %}
```

##### 使用游标连接数据库
```
@app.route('/hello/')
def hello():
    # 获取学生表中的数据
    sql = 'select * from student;'
    result = g.cursor.execute(sql)
    data = g.cursor.fetchall()
    return 'hello world'

@app.before_request
def before_request():
    # TODO: pymysql 连接数据库
    conn = pymysql.Connection(host='127.0.0.1',
                              port=3306,
                              user='root',
                              password='123456',
                              db='flask6')
    #游标
    cursor = conn.cursor()
    g.cursor = cursor
    g.conn = conn
    print('数据库在此方法中进行连接')

@app.teardown_request
def teardown_request(exception):
    #关闭数据库链接
    g.conn.close()
```
# flask中的登录注册验证
#### 启动文件manage.py
```
from flask import Flask

from flask_script import Manager

from app.models import db
from app.views import user_blueprint

app = Flask(__name__)

app.register_blueprint(blueprint=user_blueprint,url_prefix='/user')
app.secret_key = 'qwertyuoipkjhg'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@127.0.0.1:3306/flask6'
app.config['SQLALCHEMY_TRACKMODIFICATIONS'] = False

db.init_app(app)

manage = Manager(app)

if __name__ == '__main__':
    manage.run()
```
#### 2.用户模型
```
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#第一步：证明模型

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(10),unique=True,
                        nullable=False)
    password = db.Column(db.String(100),nullable=True)
    __tablename__ = 'day02_user'
```
#### 3.表单
导入
```
from flask_wtf import FlaskForm

from wtforms import StringField,SubmitField,ValidationError
from wtforms.validators import DataRequired,EqualTo

from app.models import User
```
注册表单
```
class RegisterForm(FlaskForm):

    username = StringField('用户名',validators=[DataRequired()])

    password = StringField('password',validators=[DataRequired()])
    password2 = StringField('password2',validators=[DataRequired(),
                                                    EqualTo('password','密码不一致')])

    submit = SubmitField('提交')

    def validate_username(self,field):
        #验证用户是否注册
        user = User.query.filter_by(username=field.data).first()
        if user:
            raise ValidationError('用户已经注册')
        if len(field.data) > 8:
            raise ValidationError('用户名不能超过8个字符')

        if len(field.data) < 3:
            raise ValidationError('用户名不能小于3个字符')
```
##### 验证密码是否一致，flask有一个快捷的方式
```
    password2 = StringField('password2',validators=[DataRequired(),EqualTo('password','密码不一致')])
```
登录表单
```
class LoginForm(FlaskForm):
    username = StringField('用户名',validators=[DataRequired()])
    password = StringField('password',validators=[DataRequired()])

    submit = SubmitField('提交')

    def validate_username(self,field):
        user = User.query.filter_by(username=field.data).first()
        if not user:
            raise ValidationError('该用户还没注册，请先注册')
```
#### 4.视图
注册
```
from flask import redirect, request, Blueprint,render_template,url_for

from werkzeug.security import  generate_password_hash,check_password_hash
from app.form import RegisterForm, LoginForm
from app.models import User, db

user_blueprint = Blueprint('user',__name__)

@user_blueprint.route('/register/',methods=['GET','POST'])
def register():
    form = RegisterForm()

    if request.method == 'GET':
        return render_template('register.html',form=form)

    if request.method == 'POST':
        if form.validate_on_submit():
            #验证通过
            #验证用户是否注册，验证密码和确认密码是否一致
            user = User()
            user.username = form.username.data
            user.password = generate_password_hash(form.password.data)
            db.session.add(user)
            db.session.commit()

        else:
            return redirect(url_for('user.register'))
```
登录
```
@user_blueprint.route('/login/',methods=['GET','POST'])
def login():

    form = LoginForm()
    if request.method == 'GET':
        return render_template('login.html',form=form)

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        #校验参数是否填写完整
        if not all([username,password]):
            return render_template('login.html')
        #获取用户对象
        user = User.query.filter_by(username=username).first()
        #校验密码
        if check_password_hash(user.password,password):
            return '登录成功'
        else:
            return render_template('login.html')

    else:
        return redirect(url_for('user.login'))
```
#### 5.页面
注册
```

{% extends 'base.html' %}

{% block content %}
    <form action="" method="post">
        {{ form.csrf_token }}
        {{ form.username.label }}: {{ form.username }}
        <br>
        {{ form.password.label }}: {{ form.password }}
        <br>
        {{ form.password2.label }}: {{ form.password2 }}
        <br>
        {{ form.submit }}

    </form>
{% endblock %}
```
登录
```
{% extends 'base.html' %}


{% block content %}
    <form action="" method="post">
        {{ form.username.label }}:{{ form.username }}
        <br>
        {{ form.password.label }}:{{ form.password }}
        <br>
        {{form.submit}}
    </form>
{% endblock %}
```
