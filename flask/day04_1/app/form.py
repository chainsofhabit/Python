from flask_wtf import FlaskForm

from wtforms import StringField,SubmitField,ValidationError
from wtforms.validators import DataRequired,EqualTo

from app.models import User


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

        #验证密码是否相同

class LoginForm(FlaskForm):
    username = StringField('用户名',validators=[DataRequired()])
    password = StringField('password',validators=[DataRequired()])

    submit = SubmitField('提交')

    def validate_username(self,field):
        user = User.query.filter_by(username=field.data).first()
        if not user:
            raise ValidationError('该用户还没注册，请先注册')




