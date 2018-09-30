def menu():
    print('= ' * 30)
    print('\twelcome to the student management system')
    print('1.添加学生信息')
    print('2.查看学生信息')
    print('3.删除学生信息')
    print('4.修改学生信息')
    print('5.退出系统')
    print('=' * 30)
student = []
while True:
    menu()
    number = int(input('输入选项：'))
    # 添加学生信息
    if number == 1:
        name = input('输入学生姓名：')
        sex = input('输入学生性别：')
        id = int(input('输入学生学号：'))
        person = {'姓名':name,'性别':sex,'学号':id}
        student.append(person)
        print('学生信息添加成功')
        # print(py_class)
        # number = int(input('输入选项：'))
    # 2.显示学生信息
    elif number == 2:
        if len(student) == 0:
            print('请先添加学生信息！！')
        else:
            print(student[:])
    #         for x in student:
    #             print('姓名：%s  年龄：%s   学号：%d' % (x['name'],x['sex'],x['id']))
    # 删除学生信息
    elif number == 3:
        del_name = input('输入删除的学生姓名：')
        Y = y = True
        N = n = False
        for item in student[:]:
            # print(item)
            if item['姓名'] ==del_name:
                student.remove(item)
                print('删除成功！！')
                # print('学生信息为:%s' % item)
                # choise = input('是否删除该学生信息(Y/N)：')
                # if choise == Y:
                #
                #     student.remove(item)
                #     print('删除成功')
                # else:
                #     break

    # 修改学生信息
    elif number == 4:
        change_name = input('输入想要修改学生姓名：')
        for item in student[:]:
            if item['姓名'] == change_name:
                change_name = input('输入修改后学生姓名：')
                change_sex = input('输入修改后学生性别：')
                change_id = int(input('输入修改后学生学号：'))
                new_student = {'姓名': change_name, '性别': change_sex, '学号': change_id}
                item.update(new_student)
                print('修改成功！！')

    elif number == 5:
        print('已退出系统')
        break

def save():
    stuifo = open('./student.txt','a',encoding = 'utf-8')
    for item in student:
        information = student[:]
        stuifo.write(information)
    stuifo.close()

import os
def read():
    r = open('./student.txt','r',encoding='utf-8')
    content = r.readline()
    while content:
        print(content)
        content = r.readline()
    r.close()