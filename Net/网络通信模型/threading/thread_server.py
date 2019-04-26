from socket import *
from threading import Thread

# 服务端地址
HOST = '0.0.0.0'
PORT = 1111
ADDR = (HOST, PORT)


def handle(connfd):
    print("Connect from:", connfd.getpeername())
    while True:
        data = connfd.recv(1024)
        if not data:
            break
        print(data.decode())
        connfd.send(b'ok')
    connfd.close()

# 创建套接字
s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(ADDR)
s.listen(5)

# 循环等待客户端连接
while True:
    try:
        c, addr = s.accept()
    except KeyboardInterrupt:
        s.close()
        break
    except Exception as e:
        print(e)
        break
    
    # 创建新的线程处理客户端
    t = Thread(target=handle, args=(c,))
    t.setDaemon(True)  # 分支线程会随主线程退出
    t.start()
