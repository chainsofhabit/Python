## 多对多关系
##### 创建课程表
(代码运行后自动在数据库中创建中间表)

    def add_stu_course(request):
    if request.method == 'GET':
        cous = Course.objects.all()
        return render(request,'course.html',{'cous':cous})

    if request.method == 'POST':
        #获取课程id和学生id
        c_id = request.POST.get('cous_id')
        s_id = request.GET.get('stu_id')

        stu = Student.objects.get(pk=s_id)
        #设置学生和课程的关联关系
        couse = Course.objects.get(pk=c_id)
        stu.course_set.add(couse)
        # return HttpResponse('选课成功')
        return HttpResponseRedirect('/all_stu/')
        #HttpResponseRedirect点击提交后直接跳转至学生信息页面
        
##### 选课页面

    <body>
    <form action="" method="post">
        <select name="cous_id">
            {% for cou in cous %}
                <option value="{{ cou.id }}">
                    {{ cou.c_name }}
                </option>
            {% endfor %}
        </select>
        <input type="submit" value="提交">
    </form>
    </body>


## 继承
### 模板

标签：{% tag %} {% endtag %}
标签内包括for/if/ifequal/extends/block/comment,其中除了extends外其余的都要在后面加endtag语句

例如:
```
{% extends 'base.html' %}

{% block title %}
    我是首页
{% endblock %}
```
变量:
```
{{ var }}
父模板：block块，挖坑
{% block xxx %}
{% endblock %}
子模板index.html
{% extends 'base.html' %}
{% block xxx %}
<p>xxxddd</p>
{% endblock %}
{{ block.super }}:将block块之前定义的内容拿过来
```
##### 引入CSS(两种方法)
```
{% block css %}
    #方法一
    <link href="/static/css/index.css" rel="stylesheet">
    #方法二
    {% load static %}
    <link href="{% static 'css/index.css' %}" rel="stylesheet">
{% endblock css %}
```
#### setting.py文件中添加代码
```
STATIVFILES_DIRS = [os.path.join(BASE_DIR,"STATIC")]
```
##### 引入JS
```
{% block js %}
    <script src="https://code.jquery.com/jquery-3.1.1.min.js"></script>
{% endblock %}
```


### 注解
django中单行注解用{# #}

如：

    {# 注解1 #}
    {# 注解2 #}
    {# 注解3 #}
    
### 常用过滤器
#### 1.safe
safe：当系统设置autoescaping打开的时候，该过滤器使得输出不进行escape转换。使用形式：{{value | safe}}
#### 2.date 
{{ stu.create_time | date:'Y年m月d日 H:m:s' }}
#### 3.last

last：返回列表/字符串中的最后一个元素。使用形式：{{ value | last }}
#### 4.lower

lower：将一个字符串转换成小写形式。使用形式：{{value | lower}}
#### 5.upper

upper：转换一个字符串为大写形式.使用形式：{{value | upper}}