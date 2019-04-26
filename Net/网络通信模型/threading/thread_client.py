from socket import *
from threading import Thread
import signal

ADDR = "127.0.0.1"
PORT = 1111
signal.signal(signal.SIGCHLD,signal.SIG_IGN)


server_addr = (ADDR,PORT)
# 创建套接字
sockfd = socket()
sockfd.connect(server_addr)

def handle(sockfd):
    while True:
        data = input(">>")
        if data.encode() == "##":
            sockfd.close()
            break
        sockfd.send(data.encode())
        data = sockfd.recv(1024)
        print(data.decode())


# 创建新的线程处理客户端
t = Thread(target=handle, args=(sockfd,))
t.start()