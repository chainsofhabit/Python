
from django import forms

from user.models import User

class UserRegisterForm(forms.Form):
    #定义一个name字段设置name字段的最大值和最小值
    #required是否必填，required=True必填项
    name = forms.CharField(max_length=10,min_length=2,required=True,
                           error_messages={
                               'required':'注册姓名必填',
                               'min_length':'账号不能短于两个字符',
                               'max_length':'账号长度不能超过十个字符'

                           })
    pw = forms.CharField(max_length=30,required=True,
                         error_messages={
                             'required':'密码必填',
                             'max_length': '密码长度不能超过三十个字符'
                         })
    pw2 = forms.CharField(max_length=30,required=True,
                          error_messages={
                              'required':'确认密码必填',
                              'max_length': '密码长度不能超过三十个字符'
                          })

    def clean(self):
        #获取用户名，用于校验改用户是否已经注册
        name = self.cleaned_data.get('name')
        #校验用户是否已经注册
        user = User.objects.filter(name=name.cleaned_data).first()
        if user:
            raise forms.ValidationError({'name':'该账号已经注册'})
        #验证密码是否一致
        if self.cleaned_data.get('pw') != self.cleaned_data.get('pw2'):
            raise forms.ValidationError({'pw':'密码不一致'})
        return self.cleaned_data