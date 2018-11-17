from flask import Blueprint,render_template,request
from sqlalchemy import and_,not_,or_
from app.models import db, Student, Grade

blue = Blueprint('app',__name__)

# @blue.route('/')
# def hello():
#     return 'hello'



@blue.route('/create_db/')
def create_db():
    db.create_all()
    return '创建成功'

@blue.route('/add_stu/',methods=['POST'])
def add_stu():
    #插入数据
    stu = Student()
    stu.s_name = '咻咻'
    # db.session.add(stu)
    # db.session.commit()
    stu.save()
    return '创建学生成功'

@blue.route('/del_stu/',methods=['DELETE'])
def del_stu():
    #删除数据
    stu = Student.query.filter(Student.s_name == '咻咻').first()
    db.session.delete(stu)
    db.session.commit()
    return '删除学生成功'

@blue.route('/up_stu/',methods=['PATCH'])
def up_stu():
    #第一种方式
    # stu = Student.query.filter(Student.s_name == '笑笑').first()
    # stu.s_name = '大傻子'
    # stu.save()
    #第二种方法
    Student.query.filter(Student.s_name == '大傻子').update({'s_name':'二傻子'})
    db.session.commit()

    return '更新成功'

@blue.route('/sel_stu/',methods=['GET'])
def sel_stu():
    # filter(模型名，字段 == '值')
    #filter_by(字段 = '值')
    stu = Student.query.filter_by(s_name='二傻子').first()
    # all():查询所有的结果，返回结果列表
    # first():返回对象
    # 注意：不要写all().first()



    # stu = Student.query.filter(Student.id == 1).first()
    # 查询id为1的学生，使用get()方法
    # get():get获取主键所在行的对象，如果获取不到返回空
    stu = Student.query.get(1)

    #order_by():排序
    # 降序：-id,id desc
    # 升序：id,id asc
    stu = Student.query.order_by('-id')

    #使用运算符
    # Django的ORM中:filter(s_name__contains = '111')
    # Flask的SQLAlchemy中：filter(模型名.s_name.contains(''))

    #例：模糊查询学生中包含'三'的学生信息,contains
    # stus = Student.query.filter(Student.s_name.contains('三')).all()

    #startwith,endswith,like _和%,contains

    stus = Student.query.filter(Student.s_name.startswith('二')).all()
    stus = Student.query.filter(Student.s_name.endswith('子')).all()
    #包含张
    stus = Student.query.filter(Student.s_name.like('%张%')).all()
    #第二个字是张
    stus = Student.query.filter(Student.s_name.like('_张%')).all()
    #第一个字为张
    stus = Student.query.filter(Student.s_name.like('张%')).all()
    stus = Student.query.filter(Student.s_name.like('%张')).all()
    #in_():查询某个范围之内的对象
    stus = Student.query.filter(Student.id.in_([1,2,3,4,5])).all()

    #查询id大于3的学生信息，__gt__
    # 大于 __gt__,大于等于 __ge__
    # 小于 __lt__,小于等于 __le__
    stus = Student.query.filter(Student.id.__gt__(3)).all()
    stus = Student.query.filter(Student.id > 3).all()

    #分页
    page = request.args.get('page',1)
    paginate = Student.query.paginate(int(page),3)
    stus = paginate.items

    # return render_template('stus.html',stus=stus,paginate=paginate)

    #查询性别为男，且姓名中包含'子'的学生信息
    stus = Student.query.filter(Student.gender == 1,
                                Student.s_name.contains('子')).all()

    # and_且, not_非, or_或
    stus = Student.query.filter(and_(Student.gender == 1,
                                Student.s_name.contains('子'))).all()

    stus = Student.query.filter(or_(Student.gender == 1,
                                Student.s_name.contains('成'))).all()

    stus = Student.query.filter(not_(Student.gender == 1),
                                and_(Student.s_name.contains('大'))).all()


    stus_names = [stu.s_name for stu in stus]
    return str(stus_names)

# 添加班级信息
@blue.route('/add_grade/',methods=['POST'])
def add_grade():
    grades = ['大一','大二','大三','大四']
    g_list = []
    for i in grades:
        g = Grade()
        g.g_name = i
        # db.session.add(g)
        g_list.append(g)
    db.session.add_all(g_list)
    db.session.commit()
    return '创建班级成功'

# 学生指定班级


#作业：
#正向查询：通过学生查找班级
@blue.route('/select_gda/<int:id>/')
def select_gda(id):
    stu = Student.query.get(id)
    grade = stu.stu
    return '查询成功'
    # return render_template('student_grade.html',grade=grade,stu=stu)
#反向查询：通过班级查找学生
@blue.route('/select_stu/<int:id>/')
def select_stu(id):
    grade = Grade.query.get(id)
    stus = grade.student
    # return '查询成功'
    return render_template('grade_student.html',stus=stus,grade=grade)