import gevent
from gevent import monkey
monkey.patch_all()    # 需要在之后导入socket
from socket import *
def handle(c):
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b"ok")

# 创建套接字
s = socket()
s.bind(('0.0.0.0',1111))
s.listen(10)

while True:
    c,addr = s.accept()
    print("Connect from",addr)
    #handle(c)
    gevent.spawn(handle, c)

s.close()
