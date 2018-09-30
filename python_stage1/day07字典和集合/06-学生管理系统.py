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
    py_class = {
        'student': []
    }
    # 添加学生信息
    if number == 1:
        new_name = input('输入学生姓名：')
        new_sex = input('输入学生性别：')
        new_id = int(input('输入学生学号：'))
        new_student = {'name': new_name, 'sex': new_sex, '学号': new_id}
        py_class['student'].append(new_student)
        print('学生信息添加成功')
        # print(py_class)
        # number = int(input('输入选项：'))
    # 2.显示学生信息
    elif number == 2:
        print(py_class['student'])
    # 删除学生信息
    elif number == 3:
        del_name = input('输入删除的学生姓名：')
        all_student = py_class['student']
        for student_dict in all_student[:]:
            if student_dict['name'] == del_name:
                all_student.remove(student_dict)
        print('学生已删除')
        break

    # 修改学生信息
    elif number == 4:
        change_name = input('输入想要修改学生姓名')
        for student_dict in all_student[:]:
            if student_dict['name'] == change_name:
                change_name = input('输入修改后学生姓名：')
                change_sex = input('输入修改后学生性别：')
                change_id = int(input('输入修改后学生学号：'))
                new_student = {'name': change_name, 'sex': change_sex, '学号': change_id}
                py_class['student'].append(new_student)
    elif number == 5:
        break

# 声明一个列表保存所有学生
# all_student = []
# #添加学生（一个学生对应一个字典）
# while True:
#     name = input('姓名：')
#     age = input('年龄：')
#     id = input('学号：')
#     student = {'name': name, '年龄': age, '学号': id}
#     all_student.append(student)
#     print('添加成功')
#     print('1.继续\n2.退出')
#     value = input('>>>')
#     if value == '2':
#         break
# print(all_student)
#
# #修改学生信息
# name = input('输入要修改的学生姓名：')
# #查找
# for stu in all_student:
#     if stu['name'] != name:
#         continue
#     print(stu)
#     value = input('是否需要修改该学生信息（Y/N）:')




