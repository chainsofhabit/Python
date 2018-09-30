# import file_manager
#
# file_name = "user_info.json"  #保存所有的用户信息的文件
# key_user_name = "user_name"
# key_password = "passrord"
# #=========注册=========#
# """
# 为了下次打开系统的时候能够正常登陆，注册成功的信息需要保存
# 保存用户名和密码
# 一个系统可以注册多个用户，可以用列表保存多个用户。通过字典来保存每个用户的用户名和密码
# [
#     {"user_name":"用户名","pass_word":"密码"}，
# ]
# 保存到userinfo.json中
# """
# def is_register(user_name):
#     """
#     判断指定用户是否已经注册过
#     :param user_name:
#     :return:
#     """
#     all_user = file_manager.read_json_file(file_name)
#     if not all_user:
#         return False
#     for user in all_user:
#         if user[key_user_name] == user_name:
#             return True
#     return False
#
# def get_all_user():
#     all_user = file_manager.read_json_file(file_name)
#     if all_user:
#         return all_user
#     return []
# def register():
#     # 输入用户名
#     while True:
#
#         user_name = input("请输入一个用户名(3-10)位:")
#         #判断是否符合格式要求
#         if not 3<= len(user_name)<=10:
#             print("输入有误，请重新输入！")
#             continue
#         #判断是否已经注册过
#         if is_register(user_name):
#             print("%s,已经注册过，请重新输入" % user_name)
#             continue
#         print("用户名可用！")
#         break
#
#         #2.输入密码
#     while True:
#         passeord = input("请输入密码（6-16位）:")
#         if not 6 <= len(passeord) <= 16:
#             print("密码输入有误，请重新输入！")
#             continue
#         re_password = input("确认密码:")
#         if passeord != re_password:
#             print("两次输入不一致，请重新输入")
#             continue
#         break
#         #3.保存用户名和密码
#     all_user = get_all_user()
#     all_user.append({key_user_name:user_name,key_password:passeord})
#     re = file_manager.write_json_file(file_name,all_user)
#     if re:
#         print("注册成功")
#     else:
#         print("注册失败")
# #=========登录==========
#
# def login():
#     """
#     登录
#     :return:
#     """
#     user_name = input("输入用户名:")
#     password = input("请输入密码:")
#
#     #1.看输入的用户是否已经注册过
#     all_user = get_all_user()
#     for user in all_user:
#         if user[key_user_name] == user_name:
#             if user[key_password] == password:
#                 print("登录成功")
#                 return user_name
#             else:
#                 print("密码错误，登录失败")
#                 # return None
#     print("没有注册，登录失败！")
#     return None
#
#
#
# #========主页==============
# import student_system
# def show_main_page():
#     while True:
#
#         print(file_manager.read_text_file("login.txt"))
#         value = input("请选择（1-3）:")
#
#
#         if value == "3":
#             break
#
#         #2.注册
#         elif value == "2":
#             register()
#         elif value == "1":
#             # print("登录")
#             user_name = login()
#             if user_name:
#                 student_system.user_name = user_name
#                 student_system.main_page()
#                 # print("进入学生管理系统")
#         else:
#             print("输入有误，请重新选择！！")
# #1.显示主界面
# show_main_page()



import file_manager

# 全局变量
file_name = 'user_info.json'  # 保存所有用户的信息的文件

key_user_name = 'user_name'
key_password = 'password'
# ==========================注册=================
"""
为了下次打开系统的时候能够正常登录，注册成功的信息需要保存。保存用户名和密码
一个系统可以注册多个用户，可以用列表保存多个用户。通过字典来保存每个用户名和密码
[
    {'user_name':'用户名','password':'密码'}
]
保存到userinfo.json中
"""
def is_register(user_name):
    """
    判断指定用户名是否已经注册过
    :param user_name:
    :return:
    """
    all_user = file_manager.read_json_file(file_name)
    if not all_user:
        return False
    for user in all_user:
        if user[key_user_name] == user_name:
            return True
    return False

def get_all_user():
    """
    获取所有的用户
    :return:
    """
    all_user =  file_manager.read_json_file(file_name)
    if all_user:
        return all_user
    return []

def register():
    # 1.输入用户名
    while True:
        user_name = input('请输入一个用户名(3-10位)：')
        # 判断是否符合格式要求
        if not 3 <= len(user_name) <= 10:
            print('输入有误，请重新输入！')
            continue
        # 判断是否已经注册过
        if is_register(user_name):
            print('%s,已经注册过，请重新输入！'% user_name)
            continue
        print('用户名可用！')
        break

    # 2.输入密码
    while True:
        password = input('请输入密码（6-16）:')
        if not 6 <= len(password) <= 16 :
            print('输入密码有误，请重新输入！')
            continue
        re_password = input('确认密码：')
        if password != re_password:
            print('和第一次输入的密码不一样，请重新输入！')
            continue
        break
    #3. 保存用户名和密码
    all_user = get_all_user()
    all_user.append({key_user_name:user_name,key_password:password})
    re = file_manager.write_json_file(file_name,all_user)
    if re:
        print('注册成功！')
    else:
        print('注册失败！')
# =====================登录=====================
def login():
    """
    登录
    :return:
    """
    user_name = input('请输入用户名：')
    password = input('请输入密码：')
    #1.看输入的用户名是否已经注册过
    all_user = get_all_user()
    for user in all_user:
        if user[key_user_name] == user_name:
            if user[key_password] == password:
                print('登录成功！')
                return user_name
            else:
                print('密码错误，登录失败！')
    print('没有注册，登录失败！')
    return None


# =========================主页==================
import student_system
def show_main_page():
    while True:
        print(file_manager.read_text_file('login.txt'))
        value = input('请选择（1-3）：')
        # 1.退出
        if value == '3':
            break
        #2.注册
        elif value == '2':
            register()

        elif value == '1':
            user_name = login()
            if user_name:
                # 如果登录成功就进入管理系统
                student_system.user_name = user_name
                student_system.main_page()


        else:
            print('输入有误，重新选择!')

# 1.显示登录界面（主界面）
if __name__ == '__main__':
    #1.显示登录界面（主界面）
    show_main_page()