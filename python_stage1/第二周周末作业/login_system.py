def login(username,password):
    f1 = open('./login.txt','r',encoding="utf-8")
    for line in f1:
        line = line.strip()  #去除两端空格及换行符
        line_list = line.split("$")   #用$符号分割
        if username == line_list[0] and password ==line_list[1]:
            return True
    return False
    f1.close()
def register():
    while True:
        user_name = input("请输入用户名：")
        password = input("请输入密码：")
        f = open("./wjp.txt","r",encoding="utf-8")
        f1 = f.read()

def main():
    print("1：登录\n2:注册")
    inp= int(input("请输入您的选项:"))

    user = input('请输入用户名：')
    pwd = input('请输入密码：')

    if inp == "1":
        login()
        is_login = login(user,pwd)
        if is_login:
            print('登录成功！')
        else:
            print('登录失败！！')
    if inp == "2":
        register()
        result = register(user,pwd)
        if result:
            print('注册成功!!')
        else:
            print('注册失败！！')
main()