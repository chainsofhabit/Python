import socket
def creat_client():
    client = socket.socket()

    client.connect(("10.7.153.123",8080))
    # number = 0
    while True:
        data = client.recv(1024)
        receive_data = data.decode(encoding="utf-8")
        print(receive_data)
        if receive_data == "拜拜":
            break
        massage = input("客户端:")
        client.send(massage.encode())
        if massage == "拜拜":
            break
    client.close()
# creat_client()