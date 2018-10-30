## 1.使用中间件代替装饰器，做注册登录验证
##### 1.1导入所需要用的包
```
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin

from user.models import UserToken
```
##### 1.2定义一个中间件
```
class AuthMiddleware(MiddlewareMixin):
```
##### 1.3在setting文件中添加中间件(最后一行为添加的中间件)
```
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'utils.middleware.AuthMiddleware'
]
```
##### 1.4执行代码
```
def process_request(self,request):
    #做登录验证
    #屏蔽掉登录和注册的url，不需要做登录验证
    not_check = ['/user/login/','/user/register/']
    path = request.path

    if path in not_check:
        #不继续执行以下登录验证的代码，直接去执行视图函数
        return None
    token = request.COOKIES.get('token')
    if not token:
        # cookie中没有登录的标识符，跳转到登录页面
        return HttpResponseRedirect(reverse('user:login'))
    user_token = UserToken.objects.filter(token=token).first()

    if not user_token:
        # token标识符有误，跳转到登录页面
        return HttpResponseRedirect(reverse('user:login'))
    #给全局request对象修改user属性值，修改为当前登录系统用户
    request.user = user_token.user
    return None
```
## 2.文章的上传与显示
##### 2.1 urls文件中 将media文件夹解析为静态文件夹，该文件夹主要用于存储上传的媒体文件，图片，音频等
```
#django在debug为True的情况下，就可以访问media文件夹下的内容
urlpatterns += static(MEDIA_URL,document_root=MEDIA_ROOT)
```
##### 2.2setting文件中配置media路径
```
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')
```
##### 2.3数据库配置
```
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=20)
    desc = models.CharField(max_length=150)
    img = models.ImageField(upload_to='article')
    create_time = models.DateTimeField(auto_now_add=True)


    class Meta:
        db_table = 'article'
```
##### 2.5templates文件中添加上传文章和显示文章的HTML文件
articles.html(上传文章)
```
{% block title %}
    上传文章
{% endblock %}

{% block content %}
    <form action="" method="post" enctype="multipart/form-data">
        标题:<input type="text" name="title">
        <br>
        描述:<input type="text" name="desc">
        <br>
        图片:<input type="file" name="img">
        <br>
        <input type="submit" value="提交">
    </form>
{% endblock %}
```
show_articles.html(显示文章)
```

{% extends 'base.html' %}

{% block title %}
    显示文章
{% endblock %}

{% block content %}
    标题: {{ article.title }}<br>
    描述: {{ article.desc }}<br>
    图片: <br><img src="/media/{{ article.img }}">
{% endblock %}
```
##### 2.6 user目录下urls文件中添加url 
```
#上传文章
url(r'^add_article/',views.add_article,name='add_article'),
#查看文章
url(r'^show_article/(\d+)/',views.show_article,name='show_article'),

```
##### 2.7 views视图中定义函数
添加文章
```
def add_article(request):
    if request.method == 'GET':
        return render(request,'articles.html')

    if request.method == 'POST':
        #获取数据
        img = request.FILES.get('img')
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        #创建文章
        Article.objects.create(img=img,title=title,desc=desc)


        return HttpResponse('创建图片成功')
```
显示文章
```
def show_article(request,id):
    if request.method == 'GET':
        article = Article.objects.get(pk=id)

        return render(request,'show_articles.html',{'article':article})
```
## 3.分页显示
##### 3.1定义一个分页显示的网页arts.html
添加了上一页和下一页的按钮,并将分页显示的页码作为链接
```
{% extends 'base.html' %}

{% block content %}
    {% for art in arts %}
        id: {{ art.id }}
        标题: {{ art.title }}
        描述: {{ art.desc }}
        <br>
    {% endfor %}
<br>
<p>
    {% if arts.has_previous %}
        <a href="{% url 'user:articles' %}?page={{ arts.previous_page_number }}">上一页</a>
    {% endif %}

    {% for i in arts.paginator.page_range %}
        <a href="{% url 'user:articles' %}?page={{ i }}">{{ i }}</a>
    {% endfor %}

    {% if arts.has_next %}
        <a href="{% url 'user:articles' %}?page={{ arts.next_page_number }}">下一页</a>
    {% endif %}
</p>
{% endblock %}
```
##### 3.3user文件下的urls文件添加url
```
#文章列表
url(r'^articles/',views.articles,name='articles')

```
##### 3.3定义分页显示的函数
```
def articles(request):
    if request.method == 'GET':

        page = request.GET.get('page',1)
        #查询所有文章对象，并进行分页
        articles = Article.objects.all()
        #将所有文章进行分页，每一页最多4条数据
        paginator = Paginator(articles,4)
        #获取哪一页的文章信息
        arts = paginator.page(page)
        return render(request,'arts.html',{'arts':arts})
```
##### 3.4 debug下检查分页的命令
```
#是否有上一页
arts.has_previous()
#是否有下一页
arts.has_next()
#上一页页码
arts.previous_page_number()
#下一页页码
atrs.next_page_number()
#当前页码
arts.number
```
## 4.添加日志
##### 4.1 setting文件下配置日志
```
LOGGING = {
    'version':1,
    # True表示禁用日志
    'disable_existing_loggers':False,
    # 指定写入到日志文件中的日志格式
    #格式化
    'formatters':{
        'default':{
            'format': '%(name)s %(asctime)s %(message)s'
        }
    },
    #写入文件里的手笔
    'handlers':{
        'console':{
            'level': 'INFO',
            # 定义存储日志的文件
            'filename': '%s/log.txt' % os.path.join(BASE_DIR,'logs'),
            # 指定写入日志中信息的格式
            'formatter': 'default',
            # 指定日志文件超过5M就自动做备份
            'class': 'logging.handlers.RotatingFileHandler',
            'maxBytes': 5 * 1024 * 1024,
        }
    },
    'loggers':{
        '':{
            'handlers':['console'],
            'level':'INFO'
        }
    },
}
```
##### 4.2 添加logs文件夹用于保存日志文件log.txt

##### 4.3 utils文件夹下middleware.py文件中添加中间件代码
```
class LoggingMiddleware(MiddlewareMixin):
    def process_request(self,request):
        # 记录当前请求访问服务器的时间，请求参数，请求内容....
        request.init_time = time.time()
        request.init_body = request.body
        return None
    def process_response(self,request,response):
        try:
            # 记录返回响应的时间和访问服务器的时间差，记录返回状态码...
            times = time.time() - request.init_time
            # 响应状态码
            code = response.status_code
            # 响应内容
            res_body = response.content
            # 请求内容
            req_body = request.init_body

            #日志信息
            msg = '%s %s %s %s' % (times,code,res_body,req_body)
            # 写入日志
            logging.info(msg)
        except Exception as e:
            logging.critical('log error,Exception:%s' % e)

        return response
```
##### 注意：记得在setting文件中添加中间件
##### 完成后随意访问任何一个网页，都能够在日志文件中看到访问的记录
```
root 2018-10-30 16:27:20,397 0.0500030517578125 200 b'<!DOCTYPE html>\n<html lang="en">\n<head>\n    <meta charset="UTF-8">\n    <title>\n        \n        \n    </title>\n</head>\n<body>\n    \n    \n        id: 1\n        \xe6\xa0\x87\xe9\xa2\x98: django\n        \xe6\x8f\x8f\xe8\xbf\xb0: django \xe6\xa1\x86\xe6\x9e\xb6\xe5\xad\xa6\xe4\xb9\xa0\n        <br>\n    \n        id: 2\n        \xe6\xa0\x87\xe9\xa2\x98: python\n        \xe6\x8f\x8f\xe8\xbf\xb0: python\xe5\x9f\xba\xe7\xa1\x80\xe5\xad\xa6\xe4\xb9\xa0\n        <br>\n    \n        id: 3\n        \xe6\xa0\x87\xe9\xa2\x98: html\n        \xe6\x8f\x8f\xe8\xbf\xb0: html css \xe5\x9f\xba\xe7\xa1\x80\xe5\xad\xa6\xe4\xb9\xa0\n        <br>\n    \n        id: 4\n        \xe6\xa0\x87\xe9\xa2\x98: html\n        \xe6\x8f\x8f\xe8\xbf\xb0: html js\xe5\x9f\xba\xe7\xa1\x80\n        <br>\n    \n<br>\n<p>\n    \n\n    \n        <a href="/user/articles/?page=1">1</a>\n    \n        <a href="/user/articles/?page=2">2</a>\n    \n        <a href="/user/articles/?page=3">3</a>\n    \n\n    \n        <a href="/user/articles/?page=2">\xe4\xb8\x8b\xe4\xb8\x80\xe9\xa1\xb5</a>\n    \n</p>\n\n</body>\n</html>' b''
root 2018-10-30 16:28:14,046 0.03800225257873535 200 b'<!DOCTYPE html>\n<html lang="en">\n<head>\n    <meta charset="UTF-8">\n    <title>\n        \n        \n    </title>\n</head>\n<body>\n    \n    \n        id: 5\n        \xe6\xa0\x87\xe9\xa2\x98: html\n        \xe6\x8f\x8f\xe8\xbf\xb0: html jquary\n        <br>\n    \n        id: 6\n        \xe6\xa0\x87\xe9\xa2\x98: \xe5\x8d\x83\xe9\x94\x8b\n        \xe6\x8f\x8f\xe8\xbf\xb0: \xe4\xbb\xbf\xe4\xbd\x9b\xe5\x9b\x9e\xe5\x88\xb0\xe4\xba\x86\xe9\xab\x98\xe4\xb8\xad\xe7\x94\x9f\xe6\xb4\xbb\n        <br>\n    \n        id: 7\n        \xe6\xa0\x87\xe9\xa2\x98: python1806\n        \xe6\x8f\x8f\xe8\xbf\xb0: \xe6\x97\xb6\xe9\x97\xb4\xe5\xb7\xb2\xe7\xbb\x8f\xe8\xbf\x87\xe5\x8d\x8a\xef\xbc\x8c\xe4\xb8\x94\xe8\xa1\x8c\xe4\xb8\x94\xe7\x8f\x8d\xe6\x83\x9c\n        <br>\n    \n        id: 8\n        \xe6\xa0\x87\xe9\xa2\x98: \xe9\x9a\x8f\xe4\xbe\xbf\xe6\x83\xb3\xe7\x9a\x84\xe6\xa0\x87\xe9\xa2\x98\n        \xe6\x8f\x8f\xe8\xbf\xb0: \xe5\xae\x9e\xe5\x9c\xa8\xe4\xb8\x8d\xe7\x9f\xa5\xe9\x81\x93\xe5\x86\x99\xe5\x95\xa5\n        <br>\n    \n<br>\n<p>\n    \n        <a href="/user/articles/?page=1">\xe4\xb8\x8a\xe4\xb8\x80\xe9\xa1\xb5</a>\n    \n\n    \n        <a href="/user/articles/?page=1">1</a>\n    \n        <a href="/user/articles/?page=2">2</a>\n    \n        <a href="/user/articles/?page=3">3</a>\n    \n\n    \n        <a href="/user/articles/?page=3">\xe4\xb8\x8b\xe4\xb8\x80\xe9\xa1\xb5</a>\n    \n</p>\n\n</body>\n</html>' b''
root 2018-10-30 16:28:15,266 0.0630035400390625 200 b'<!DOCTYPE html>\n<html lang="en">\n<head>\n    <meta charset="UTF-8">\n    <title>\n        \n        \n    </title>\n</head>\n<body>\n    \n    \n        id: 9\n        \xe6\xa0\x87\xe9\xa2\x98: django\n        \xe6\x8f\x8f\xe8\xbf\xb0: day06 \xe8\x87\xaa\xe5\xb8\xa6\xe7\x9a\x84\xe7\x99\xbb\xe5\xbd\x95\xe6\xb3\xa8\xe5\x86\x8c\xe9\xaa\x8c\xe8\xaf\x81\n        <br>\n    \n        id: 10\n        \xe6\xa0\x87\xe9\xa2\x98: \xe4\xba\xac\xe4\xb8\x9c\n        \xe6\x8f\x8f\xe8\xbf\xb0: \xe9\xa6\x96\xe9\xa1\xb5\xe7\xbb\x83\xe4\xb9\xa0\n        <br>\n    \n<br>\n<p>\n    \n        <a href="/user/articles/?page=2">\xe4\xb8\x8a\xe4\xb8\x80\xe9\xa1\xb5</a>\n    \n\n    \n        <a href="/user/articles/?page=1">1</a>\n    \n        <a href="/user/articles/?page=2">2</a>\n    \n        <a href="/user/articles/?page=3">3</a>\n    \n\n    \n</p>\n\n</body>\n</html>' b''

```