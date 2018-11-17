## 模型
### 1.模型数据
1.1.启动文件manage.py
```
from app.views import blue
from app.models import db

app = Flask(__name__)

app.register_blueprint(blueprint=blue,url_prefix='/app')

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@127.0.0.1:3306/flask6'
app.config['SQLALCHEMY_TRACKMODIFICATIONS'] = False

db.init_app(app)

manage = Manager(app)

if __name__ == '__main__':
    manage.run()
```
1.2.定义一个模型
```
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Student(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    s_name = db.Column(db.String(10),unique=True,nullable=False)
    gender = db.Column(db.Boolean,default=1)
```
1.3.迁移数据库
```

@blue.route('/create_db/')
def create_db():
    db.create_all()
    return '创建成功'
```
1.4.封装方法
```
def save(self):
    db.session.add(self)
    db.session.commit()
```
### 2.数据处理
2.1.添加对象
```
@blue.route('/add_stu/',methods=['POST'])
def add_stu():
    #插入数据
    stu = Student()
    stu.s_name = '咻咻'
    # db.session.add(stu)
    # db.session.commit()
    stu.save()
    return '创建学生成功'
```
2.2.删除对象
```
@blue.route('/del_stu/',methods=['DELETE'])
def del_stu():
    #删除数据
    stu = Student.query.filter(Student.s_name == '咻咻').first()
    db.session.delete(stu)
    db.session.commit()
    return '删除学生成功'
```
2.3数据更新
```
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
```
2.4查询与排序
```
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
    return '查询成功'
```
使用运算符

Django的ORM中：filter(s_name__contains = 'xxx')

Flask的SQLAlchemy中：filter(模型名.s_name.contains(''))

例：模糊查询学生的姓名中包‘三’的学生信息，contains
```
stus = Students.query.filter(Student.s_name.contains('三')).all()
```

#startswith,endswith,like(_和%),contains
```
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

```
查询id 大于3的学生信息
```
# 大于 __gt__,大于等于 __ge__
# 小于 __lt__,小于等于 __le__
stus = Student.query.filter(Student.id.__gt__(3)).all()
stus = Student.query.filter(Student.id > 3).all()
```
分页，定义一个显示学生信息的html文件
```
<body>
    {% for stu in stus %}
        <p>id: {{ stu.id }} 姓名:{{ stu.s_name }}</p>
    {% endfor %}
    当前一共{{ paginate.pages }}页
    {% if paginate.has_prev %}
        <a href="{{ url_for('app.sel_stu') }}?page={{ paginate.prev_num }}">上一页</a>
    {% endif %}

    {% for i in paginate.iter_pages() %}
        <a href="{{ url_for('app.sel_stu') }}?page={{ i }}">{{ i }}</a>
    {% endfor %}

    {% if paginate.has_next %}
        <a href="{{ url_for('app.sel_stu') }}?page={{ paginate.next_num }}">下一页</a>
    {% endif %}


</body>
```
视图文件
```
page = request.args.get('page',1)
paginate = Student.query.paginate(int(page),3)
stus = paginate.items

return render_template('stus.html',stus=stus,paginate=paginate)

```