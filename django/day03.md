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
    
#### 一对一关系
新建一张学生信息的扩展表，包括学生的练习电话，籍贯等字段

    class StudentInfo(models.Model):
    tel = models.CharField(max_length=11,null=True)
    address = models.CharField(max_length=88)
    #OneToOneField  指定一对一关联关系,该字段定义在任何一个模型都可以
    stu = models.OneToOneField(Student)
    class Meta:
        db_table = 'student_info'

在网页中添加学生的扩展信息--项目文件夹中新建两个html文件（stus.html info.html），stus.html文件显示已有的学生信息，
    
    #stus.html
    <body>
    <table>
        <thead>
            <th>姓名</th>
            <th>年龄</th>
            <th>操作</th>
        </thead>
        <tbody>
            {% for stu in students %}
                <tr>
                    <td>{{stu.s_name}}</td>
                    <td>{{stu.s_age}}</td>
                    <td>
                        <a href="/add_info/?stu_id={{ stu.id }}">添加扩展信息</a>
                    </td>
                </tr>
            {% endfor %}
        </tbody>
    </table>
    </body>
    
info.html添加学生的扩展信息

    <body>
    <form action="" method="post">
        电话号码:<input type="text" name="tel">
        地址:<input type="text" name="address">
        <input type="submit" value="提交">

    </form>
    </body>
    
查询

通过学生查找扩展表信息

    def sel_info_by_stu(request):
    if request.method == 'GET':
        #通过学生查询扩展表信息
        stu = Student.objects.get(s_name = '咻咻')
        #第一种
        # info = StudentInfo.objects.filter(stu_id = stu.id)
        info = StudentInfo.objects.filter(stu=stu).first()


        #第二种 学生对象，关联的模型名的小号
        # info = stu.studentinfo
        print(info.address)
        return HttpResponse("通过学生查找扩展表信息")
        

通过扩展表内容查找学生的信息

    def sel_stu_by_info(request):
    if request.method == 'GET':
        #知道手机号码找人
        info = StudentInfo.objects.get(tel='17398087789')
        student = info.stu
        print(student.s_name)
        return HttpResponse('通过手机号查找学生的信息')
        
#### 一对多关系（学生和班级）
1.新建一个班级表

    class Grade(models.Model):
    g_name = models.CharField(max_length=10, unique=True)

    class Meta:
        db_table = 'grade'
        
2.向班级表格中添加班级信息

    def add_grade(request):
    if request.method == 'GET':
        Grade.objects.create(g_name='python1806')
        Grade.objects.create(g_name='html1705')
        Grade.objects.create(g_name='java1807')
        Grade.objects.create(g_name='test1703')
        
查询

    def sel_stu_grade(request):
    if request.method == 'GET':
        #通过学生查找班级
        stu = Student.objects.filter(s_name='小萌').first()
        grade = stu.grade

        #通过班级查找学生
        grade = Grade.objects.get(g_name='python1806')
        students = grade.student_set.all()

        return HttpResponse('查询学生和班级信息')
        
##### 注意：查询之前记得在urls.py文件中添加url
    
    
 
    


    