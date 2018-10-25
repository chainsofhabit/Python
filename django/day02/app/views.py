from django.db.models import Q,F
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect


from app.models import Student,StudentInfo,Grade,Course
# Create your views here.
def hello(request):
    return HttpResponse('千峰教育欢迎你')

def create_stu(request):
    #创建学生
    # stu = Student()
    # stu.s_name = '咻咻'
    # stu.s_age = 21
    # stu.save()

    Student.objects.create(s_name = '小王')
    Student.objects.create(s_name='小周')
    Student.objects.create(s_name='小李')
    Student.objects.create(s_name='小赵')
    Student.objects.create(s_name='小芳')
    Student.objects.create(s_name='小萌')

    return HttpResponse('创建成功')

def add_grade(request):
    if request.method == 'GET':
        Grade.objects.create(g_name='python1806')
        Grade.objects.create(g_name='html1705')
        Grade.objects.create(g_name='java1807')
        Grade.objects.create(g_name='test1703')


def sel_stu_grade(request):
    if request.method == 'GET':
        #通过学生查找班级
        stu = Student.objects.filter(s_name='小萌').first()
        grade = stu.grade

        #通过班级查找学生
        grade = Grade.objects.get(g_name='python1806')
        students = grade.student_set.all()

        return HttpResponse('查询学生和班级信息')





def sel_stu(request):
    #实现查询
    #all() 查询所有对象信息
    stus = Student.objects.all()
    # filter() 过滤
    suts = Student.objects.filter(s_name = '咻咻')

    # first() 获取第一个
    # last() 获取最后一个
    stus = Student.objects.filter(s_age=20).first()
    # get() 获取对象,容易出错
    # stus = Student.objects.get(s_age=20)
    # 查询年龄等于20,性别是女的学生的信息
    stus = Student.objects.filter(s_age=20).filter(s_gender=0)
    stus = Student.objects.filter(s_age=20, s_gender=0)

    # 模糊查询  like '%xx%'  'x%'  '%x'
    stus = Student.objects.filter(s_name__contains='小')
    stus = Student.objects.filter(s_name__startswith='咻')
    stus = Student.objects.filter(s_name__endswith='王')

    # 大于 gt/gte  小于 lt/lte
    # 年龄大于18
    stus = Student.objects.filter(s_age__gt=18)
    # 大于等于18
    stus = Student.objects.filter(s_age__gte=18)
    stus = Student.objects.filter(s_age__lt=18)
    stus = Student.objects.filter(s_age__lte=18)

    # 排序  order_by()
    # 升序
    stus = Student.objects.order_by('id')
    # 降序
    stus = Student.objects.order_by('-id')

    # 查询不满足条件的数据 exclude()
    stus = Student.objects.exclude(s_age=18)


    # Q(),alt+enter
    #非条件
    stus = Student.objects.filter(Q(s_age = 20) | Q(s_gender = 0))
    #且条件
    stus = Student.objects.filter(Q(s_age=20) & Q(s_gender=0))
    #非条件
    stus = Student.objects.filter(~Q(s_age=20))

    #查询语文成绩比数学成绩高的信息
    stus = Student.objects.filter(Chinese__gt=F('math'))

    stu_names = [stu.s_name for stu in stus]
    print(stu_names)
    return HttpResponse('查询成功')

def del_stu(request):
    #实现删除
    Student.objects.filters(s_name = '咻咻').delete()
    return HttpResponse('删除成功')

def update_stu(request):
    #实现更新
    #第一种
    # stu = Student.objects.filter(s_name='小王').first()
    #
    # stu.s_name = '王熙'
    # stu.save()

    #第二种
    Student.objects.filer(s_name='王熙').update(s_name='')

    return HttpResponse('修改成功')

def all_stu(request):
    #获取所有学生信息
    stus = Student.objects.all()
    #返回页面
    return render(request,'stus.html',{'students':stus})


def add_info(request):
    #method获取请求HTTP方式
    if request.method == 'GET':
        return render(request,'info.html')

    if request.method == 'POST':
        #获取页面中提交的手机号码和地址，并保存
        tel = request.POST.get('tel')
        address = request.POST.get('address')
        stu_id = request.GET.get('stu_id')

        #保存
        StudentInfo.objects.create(tel = tel,
                                   address = address,
                                   stu_id = stu_id)
        return HttpResponse('创建扩展表信息成功')

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

def sel_stu_by_info(request):
    if request.method == 'GET':
        #知道手机号码找人
        info = StudentInfo.objects.get(tel='17398087789')
        student = info.stu
        print(student.s_name)
        return HttpResponse('通过手机号查找学生的信息')


def add_course(request):
    #添加课程
    # if request.method == 'GET':
    #     Course.objects.create(c_name='java')
    #     Course.objects.create(c_name='python')
    #     Course.objects.create(c_name='php')
    #     Course.objects.create(c_name='c#')
    #     Course.objects.create(c_name='html')

        names = ['java','python','html','php']
        for name in names:
            Course.objects.create(c_name = name)
        return HttpResponse('课程创建成功')

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






