#定义一个添加学生信息的函数
def add():
    print('====添加学生信息====')
    name = input('输入学生姓名：')
    sex = input('输入学生性别：')
    id = int(input('输入学生学号：'))

    ifo = open('./student.txt','r',encoding='utf-8')
    f = ifo.read()
    student1 = eval(f)
    ifo.close()
    person = {'姓名': name, '性别': sex, '学号': id}
    student = student1
    student.append(person)

    stuifo = open('./student.txt', 'w', encoding='utf-8')
    stuifo.write(str(student))

    stuifo.close()
    print('学生信息添加成功')

#定义一个查看学生信息的函数
def query():
    ifo = open('./student.txt', 'r', encoding='utf-8')
    f = ifo.read()
    student1 = eval(f)
    ifo.close()
    if len(student1) == 0:
        print('请先添加学生信息！！')
    else:


        print(student1[:])

#定义一个删除学生信息的函数
def delete():
    del_name = input('输入删除的学生姓名：')
    ifo = open('./student.txt', 'r', encoding='utf-8')
    f = ifo.read()
    student1 = eval(f)
    ifo.close()
    # Y = y = True
    # N = n = False
    for item in student[:]:
        # print(item)
        if item['姓名'] == del_name:
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
            stuifo = open('./student.txt', 'w', encoding='utf-8')
            stuifo.write(str(student1))

            stuifo.close()

#定义一个修改学生信息的函数
def modify():
    change_name = input('输入想要修改学生姓名：')
    ifo = open('./student.txt', 'r', encoding='utf-8')
    f = ifo.read()
    student1 = eval(f)
    ifo.close()
    for item in student[:]:
        if item['姓名'] == change_name:
            change_name = input('输入修改后学生姓名：')
            change_sex = input('输入修改后学生性别：')
            change_id = int(input('输入修改后学生学号：'))
            new_student = {'姓名': change_name, '性别': change_sex, '学号': change_id}
            item.update(new_student)
            print('修改成功！！')
            #将学生信息写入文件中
            stuifo = open('./student.txt', 'w', encoding='utf-8')
            stuifo.write(str(student1))

            stuifo.close()


#存储学生信息函数
# def save():
#     stuifo = open('./student.txt','a',encoding = 'utf-8')
#     for student_list in student:
#         information = ''.join(student)
#         stuifo.write('information')
#         # print(stuifo)
#     stuifo.close()
# import os
# #读取学生信息函数
# def read():
#     r = open('./student.txt','r',encoding='utf-8')
#     content = r.readline()
#     # while True:
#     #
#     #     content = r.readline()
#     print(content)
#     r.close()
#声明一个列表存放学生信息
student = []

# read()
#菜单
def menu():
    print('= ' * 30)
    print('\twelcome to the student management system')
    print('1.添加学生信息')
    print('2.查看学生信息')
    print('3.删除学生信息')
    print('4.修改学生信息')
    print('5.退出系统')
    print('=' * 30)

while True:
    menu()
    number = int(input('输入选项：'))
    if number == 1:
        #添加学生信息函数
        add()
        # save()

    elif number == 2:
        #查看学生信息函数
        query()
    elif number == 3:
        #删除学生信息函数
        delete()
        # save()
    elif number == 4:
        #修改学生信息函数
        modify()
        # save()
    elif number == 5:
        print('退出程序！！')
        break

