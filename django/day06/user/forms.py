from django import forms
from django.contrib.auth.models import User


class UserRegisterForm(forms.Form):
    username = forms.CharField(max_length=10,min_length=2,
                           required=True,
                           error_messages={
                               'required':'注册姓名必填',
                               'min_length':'账号不能短于两个字符',
                               'max_length':'账号长度不能超过十个字符'
                           })
    password = forms.CharField(max_length=30, required=True,
                         error_messages={
                             'required': '密码必填',
                             'max_length': '密码长度不能超过三十个字符'
                         })

    password2 = forms.CharField(max_length=30, required=True,
                         error_messages={
                             'required': '密码必填',
                             'max_length': '密码长度不能超过三十个字符'
                         })

    def clean(self):
        user = User.objects.filter(username=self.cleaned_data.get('username')).first()
        if user:
            raise forms.ValidationError({'username':'账号已注册'})
        if self.cleaned_data.get('password') != self.cleaned_data.get('password2'):
            raise forms.ValidationError({'password':'密码不一致'})
        return self.cleaned_data

class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=10, min_length=2,
                               required=True,
                               error_messages={
                                   'required': '注册姓名必填',
                                   'min_length': '账号不能短于两个字符',
                                   'max_length': '账号长度不能超过十个字符'
                               })
    password = forms.CharField(max_length=30, required=True,
                               error_messages={
                                   'required': '密码必填',
                                   'max_length': '密码长度不能超过三十个字符'
                               })

    def clean(self):
        user = User.objects.filter(username=self.cleaned_data.get('username')).first()
        if not user:
            raise forms.ValidationError({'username':'该账号还没注册，请先注册'})

        return self.cleaned_data

# class UserIndexForm(forms.Form):
