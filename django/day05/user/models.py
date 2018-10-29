from django.db import models

class User(models.Model):
    #定义username字段，最长不能超过9个字符，唯一
    name = models.CharField(max_length=9,unique=True,verbose_name='用户名')
    #定义password字段，最长不能超过20个字符，唯一
    password = models.CharField(max_length=200)
    email = models.CharField(max_length=30,null=True)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'User'

class UserToken(models.Model):
    #标识符，用于用户访问需要登录验证页面的时候使用，检验标识符是否正确
    token = models.CharField(max_length=30,verbose_name='标识符')
    user = models.OneToOneField(User)

    class Meta:
        db_table = 'user_token'