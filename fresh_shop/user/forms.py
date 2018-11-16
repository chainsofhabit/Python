from django import forms

from user.models import User
class UserRegisterForm(forms.Form):
    username = forms.CharField(max_length=20,min_length=5,
                                required=True,error_messages={
                                    'required':'用户名必填',
                                    'max_length':'用户名长度不能超过20字符',
                                    'min_length':'用户名不能短于5字符'
                                })
    password = forms.CharField(max_length=20, min_length=8,
                          required=True, error_messages={
                              'required': '密码必填',
                              'max_length': '密码长度不能超过20字符',
                              'min_length': '密码不能短于8字符'
                          })
    password2 = forms.CharField(max_length=20, min_length=8,
                          required=True, error_messages={
                              'required': '密码必填',
                              'max_length': '密码长度不能超过20字符',
                              'min_length': '密码不能短于8字符'
                          })
    email = forms.EmailField(required=True,
                             error_messages={
                                 'required': '邮箱必填'
                             })

    def clean_user(self):
        #判断用户是否注册
        username = self.cleaned_data.get('username')
        user = User.objects.filter(username=username).first()
        if user:
            raise forms.ValidationError({'user_name':'该账号已注册'})
        if self.cleaned_data.get('password') != self.cleaned_data.get('password2'):
            raise forms.ValidationError({'password':'两次输入的密码不一致'})
        return self.cleaned_data


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=20, min_length=5,
                               required=True,
                               error_messages={
                                   'required': '用户名必填',
                                   'min_length': '用户名不能短于5个字符',
                                   'max_length': '账号长度不能超过20个字符'
                               })
    password = forms.CharField(max_length=20, required=True,min_length=8,
                               error_messages={
                                   'required': '密码必填',
                                   'max_length': '密码长度不能超过20个字符',
                                   'min_length': '密码长度不能短于8个字符'
                               })

    def clean_login(self):
        user = User.objects.filter(username=self.cleaned_data.get('username')).first()
        if not user:
            raise forms.ValidationError({'username':'该用户还未注册'})
        return self.cleaned_data
class UserAddressForm(forms.Form):
    #用户地址保存的表单验证
    signer_name = forms.CharField(required=True,error_messages={'required':'收件人必填'})
    address = forms.CharField(required=True,error_messages={'required':'详细地址必填'})
    signer_mobile = forms.CharField(required=True,error_messages={'required':'联系方式必填'})
    signer_postcode = forms.CharField(required=True,error_messages={'required':'邮编必填'})
