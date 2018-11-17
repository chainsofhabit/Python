
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
