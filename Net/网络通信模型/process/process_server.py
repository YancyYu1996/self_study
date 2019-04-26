from socket import *
from multiprocessing import Process
import signal


# 服务端地址
HOST = '0.0.0.0'
PORT = 1111
ADDR = (HOST, PORT)
signal.signal(signal.SIGCHLD, signal.SIG_IGN)


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

    # 创建新的进程处理客户端
    t = Process(target=handle, args=(c,))
    t.daemon = True  # 分支进程会随主进程退出
    t.start()
