import socket
def creat_server():
    """写一个服务器"""
    #创建套接字对象
    server = socket.socket()
    #绑定IP地址和端口
    server.bind(("10.7.153.123",8088))
    #开始监听（监听客户端的请求）
    """listen(最大个数)"""
    server.listen(512)
    while True:
        connect,addr = server.accept()
        while True:
            message = input("服务器:")
            connect.send = (message.encode)
            if message == "拜拜":
                break
            recv_dada = connect.recv(1024)
            print(str(recv_data,"utf8"))
            if recv_data == "拜拜":
                break

        connect.close()
creat_server()
