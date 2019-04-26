from select import *
from socket import *
import sys
from time import ctime
# 创建关注的IO
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(("0.0.0.0",11111))
s.listen(5)

#创建poll对象
p= poll()

iput = sys.stdin
#建立地图
fdmap = {s.fileno():s,iput.fileno():iput}

#关注io
p.register(s,EPOLLIN|EPOLLERR)
p.register(iput,EPOLLIN)

# 监控键盘

while True:
    events = p.poll()
    # 遍历events 处理IO
    for fd,event in events:
        if fd == s.fileno():
            c,addr = fdmap[fd].accept()
            print("Connect from",addr)
            with open(r"/home/tarena/test/Net/IO多路复用/log.txt","at") as fa:
                fa.write("Connect from %s \r\n"%str(addr))
                fa.flush()
            # 添加新关注的IO
            p.register(c,EPOLLIN|EPOLLHUP)
            fdmap[c.fileno()] = c
        elif fd == iput.fileno():
            data = fdmap[fd].readlines()
            with open(r"/home/tarena/test/Net/IO多路复用/log.txt","at") as fa:
                fa.write("Time : %s,Data : %s \r\n"%(ctime(),data))
                fa.flush()
        elif event & EPOLLHUP: 
            
            print("客户端退出")
            p.unregister(fd)
            fdmap[fd].close()
            del fdmap[fd]
        elif event & EPOLLIN:
            data = fdmap[fd].recv(1024)
            print(data.decode())
            with open(r"/home/tarena/test/Net/IO多路复用/log.txt","at") as fa:
                fa.write("Time : %s,ResvData : %s \r\n"%(ctime(),data.decode()))
                fa.flush()
            fdmap[fd].send(b'ok')
        
        
        