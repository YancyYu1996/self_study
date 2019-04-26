#block_io.py
#非阻塞IO测试
from socket import *
from time import sleep
#创建tcp套接字
sockfd = socket()
sockfd.bind(('127.0.0.1',8000))
sockfd.listen(3)

#设置非阻塞状态
#sockfd.setblocking(False)

#设置超时检查
sockfd.settimeout(3)
while True:
    print("waiting for connect")
    try:
        connfd,addr = sockfd.accept()
    except BlockingIOError as e:
        sleep(2)
        print(e)
        continue
    except timeout:
        print("timeout...")
    else:
        print("connect from",addr)
        data = connfd.recv(1024)

