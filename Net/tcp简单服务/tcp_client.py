# tcp_client.py
from server_conf import *
from socket import *

        
if __name__ == "__main__":
    # 创建套接字
    sockfd = socket()
    # 发起连接
    server_addr = (host,serverport)
    sockfd.connect(server_addr)
    while True:
        data = input(">>")
        sockfd.send(data.encode())   # 转换成字节串
        data = sockfd.recv(1024) 
        if data.decode() != " ":
            print("From server :",data.decode())
        else:
            print("Send message END")
            break
    else:
        sockfd.close()

