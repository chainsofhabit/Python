创建应用

    python manage.py startapp app名称
ORM object-relational-mapping 对象关系映射

生成迁移文件

    python manage.py makemigrations

将文件迁移到数据库

    python manage.py migrate
    
添加记录

    在urls.py文件中添加url
添加模型

    models.py文件中创建数据库，表字段

添加视图

    views.py数据库表添加数据，返回消息
    
## 创建新表
#### 在models.py文件中写添加表的代码

    class Student(models.Model):
        #定义s_name字段，varchar类型，最长不超过6个字符
        s_name = models.CharField(max_length=6,unique=True)
        #定义s_age字段，int类型，默认值18
        s_age = models.IntegerField(default=18)
        #定义s_gender字段，int类型
        s_gender = models.Booleanfield(default=1)
        
        class Meta:
            #定义模型迁移到数据库中的表名
            db_table = 'student'
            
#### 在setting.py文件下的INSTALLED-APPS中添加'app'

    INSTALLED_APPS = [
        'django.contrib.admin',
        .......
        'app',
    ]
    
#### 在数据库中添加记录
在view.py中导入Student对象

    from app.models import Student
    
#### 新建添加学生函数

    def create_stu(request):
        #创建学生
        stu = Student()
        stu.s_name = '李明'
        stu.s_age = 21
        stu.save()
        return HttpResponse('创建成功')
        
#### 在urls.py中添加url并执行程序

    from app import views
    urlpatterns = [
        #127.0.0.1:8080/admin/
        url(r'^admin/',views.site.urls),
        #127.0.0.1:8080/create_stu/
        url(r'^create_stu/',views.create_stu)
    ]
    
##### 添加学生

    Student.objects.create(s_name = '小王'，s_age='21',s_gender=0)
    
## 查询

#### all()查询所有对象

    stus = Student.objects.all()
    
#### filter()过滤

    stus = Student.objects.filter(s_name = '李明')

#### get()获取对象

    stus = Student.objects.get(s_age=20)

#### 模糊查询 like'%xxx%' 'x%' '%x'

    stus = Students.objects.filter(s_name__contains='李')
    或者是以什么字符开头（startwith）;以什么字符结尾（endswith）

#### 大于gt/gte  小于le/lte

    stus = Student.objects.filter(s_age__gt=18)
    
#### 排序 order_by()

    #升序
    stus = Student.objects.orderby('id')
    #降序
    stus = Student.objects.orderby('-id')
    
#### 查询不满足条件的数据 exclude()

    stus = Student.objects.exclude(s_age=18)

#### 计算统计的个数：count(),len()

    stus_count = stus.count()
    stus_count = len(stus)
            
### 关联关系
1.一对一：OneToOneField

    class A:
        id = xxxx
        b = OneToOneField(B)
    class B:
        id = xxxx
        
    已知a对象，查找b对象：a.b
    已知b对象，查找a对象：b.a
    
2.一对多：foreignKey

    class A:
        id = xxxx
        b = Foreignkey(B)
    class B:
        id = xxxx
    
    已知a对象，查找b对象:a.b
    已知b对象，查找a对象:b.a_set
    
    
    
