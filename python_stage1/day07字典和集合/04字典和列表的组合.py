#学生管理系统
#1.一个系统可以存储多个学生
# 系统应该是一个容器:列表，字典
#2.一个学生可以存储：姓名，电话，籍贯，专业，学号等
#3.添加学生
#4.删除学生
#5.修改学生信息

#.....
#什么时候使用列表  什么时候使用字典
#保存的多个数据是同一个类型的时候用列表
#例如：声明一个变量保存所有的数学成绩，声明一个变量保存所有的学生信息

#保存的多个数据的类型不同时使用字典
#声明一个变量保存一个学生的信息

#列表中有字典
student_system = [
    {'name':'stu1','age':18,'tel':121,'native_place':'重庆'},
    {'name':'stu2','age':19,'tel':123,'native_place':'成都'}
]
#取出第一个学生的籍贯
print(student_system[0]['native_place'])

#2.字典中有列表
py_class = {
    'class_name':'python1806',
    'students':[
        {'name':'stu1','age':18,'tel':121,'id':'001'},
        {'name':'stu2','age':19,'tel':123,'id':'002'}
    ]
}
#取班级名
print(py_class['class_name'])
#取第三个学生的成绩
print(py_class['students'][1]['name'])


# #在班级中添加一个学生，学生信息自己输入
name = input('输入学生姓名：')
age = int(input('输入学生年龄：'))
id = int(input('输入学生id:'))
student = {'name':name,'age':age,'id':id}
py_class['students'].append(student)
print(py_class)

#输入一个学生姓名，根据姓名删除对应学生
del_name = input('输入学生姓名:')
#获取班级所有学生
all_student = py_class['students']
#遍历取出所有学生对应的字典
for student_dict in all_student[:]:
    if student_dict['name'] == del_name:
        all_student.remove(student_dict)
print(py_class)

