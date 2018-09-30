import file_manager
user_name = ""
#========添加学生======
"""
一个账号对应管理不同的学生--不同的用户对应不同的json文件
json文件中的格式:
{
    "name":""
    "number":个数
    "all_student":[
        {"name":"age":"tel":"id"}
    ]
}
"""
key_number = "number"
key_all_student = "all_student"
key_name = "name"
key_age = "age"
key_tel = "tel"
key_id = "id"
def get_system_info():
    """
    获取系统文件内容
    :return:
    """
    system_info = file_manager.read_json_file(user_name+".json")
    if system_info:
        return system_info
    return {}
def creat_id():
    """
    产生学号
    :return:
    """
    system_info = get_system_info()
    number = system_info.get(key_number, 0)
    number += 1
    id = "py"+ str(number).rjust(4,"0")  #学号右对齐
    return id,number

def add_student():
    while True:
        name = input("姓名:")
        age = input("年龄:")
        tel = input("电话：")

        #2.产生id
        id,number = creat_id()

        #3.创建学生
        stu = {key_name:name,key_age:age,key_tel:tel,key_id:id}

        #4保存学生信息
        system_info = get_system_info()
        all_student = system_info.get(key_all_student,[])
        all_student.append(stu)


        #5.保存到文件中
        system_info[key_all_student] = all_student
        system_info[key_number] = number
        re = file_manager.write_json_file(user_name+".json",system_info)
        if re:
            print("添加成功")
        else:
            print("添加失败")

        print("1.继续添加")
        print("2.返回")
        value = input("请选择（1/2）:")
        if value == "1":
            continue
        else:
            break

#======查找学生=====
def find_student():
    print("1.查看所有学生")
    print("2.根据姓名查找学生")
    print("3.根据学号查找学生")

    all_student = get_system_info().get(key_all_student, [])
    if not all_student:
        print("目前还没有学生")
        return
    value = input("请选择（1-3）:")
    if value == "1":
        for stu in all_student:
            print("姓名:%s,学号:%s,年龄:%s,电话:%s," % (stu[key_name],\
                        stu[key_id],stu[key_age],stu[key_tel]))
    elif value == "2":
        name = input("输入姓名:")
        for stu in all_student:
            if stu[key_name] == name:
                print("姓名:%s,学号:%s,年龄:%s,电话:%s," % (stu[key_name],\
                            stu[key_id],stu[key_age],stu[key_tel]))
                break
        else:

            print("没有该学生")
    elif value == "3":
        id = input("输入学号:")
        for stu in all_student:
            if stu[key_id] == id:
                print("姓名:%s,学号:%s,年龄:%s,电话:%s，" % (stu[key_name],\
                           stu[key_id],stu[key_age],stu[key_tel]))
                break
        else:
            print("没有该学生")

#======删除======
def delete_student():
    del_name = input("输入想要删除的学生的姓名：")
    system_info = get_system_info()
    all_student = get_system_info().get(key_all_student, [])

    for stu in all_student[:]:
        if stu[key_name] == del_name:
            print("想要删除的学生信息为：姓名:%s,学号:%s,年龄:%s,电话:%s" % (stu[key_name],\
                            stu[key_id],stu[key_age],stu[key_tel]))
            value1 = input("是否删除（Y/N）:")
            if value1 == "Y":
                all_student.remove(stu)
                print("删除成功！")
                break
            else:
                break
    system_info[key_all_student] = all_student
    file_manager.write_json_file(user_name + ".json", system_info)
#===========修改=========
def modify_student():
    mod_name = input("请输入想要修改的学生姓名:")
    system_info = get_system_info()
    all_student = get_system_info().get(key_all_student, [])
    for stu in all_student[:]:
        if stu[key_name] == mod_name:
            print("想要修改的学生信息为：姓名:%s,学号:%s,年龄:%s,电话:%s" % (stu[key_name], \
                            stu[key_id], stu[key_age], stu[key_tel]))
            print("1.修改年龄；2.修改电话")
            value2 = input("请选择（1/2）：")
            if value2 == "1":
               mod_age = input("修改后的学生年龄为：")
               stu[key_age] = mod_age
               print("修改成功！！")
            elif value2 == "2":
                mod_tel = input("修改后的学生电话为:")
                stu[key_tel] = mod_tel
                print("修改成功！！")

    system_info[key_all_student] = all_student
    file_manager.write_json_file(user_name + ".json", system_info)





def main_page():
    while True:

        print(file_manager.read_text_file("system.txt"))
        value = input("请选择（1-5）:")
        if value == "5":
            break
        elif value == "1":
            add_student()
        elif value == "2":
            find_student()
        elif value == "3":
           delete_student()
        elif value == "4":
            modify_student()
        else:
            print("输入有误")
