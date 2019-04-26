from select import  select
from socket import *
import sys
from time import ctime
#创建套接字作为关注的IO
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',11111))
s.listen(5)

iput = sys.stdin
#添加到关注列表
rlist = [s,iput]
wlist = []
xlist = []


while True:
    # 监控IO
    rs,ws,xs = select(rlist,wlist,xlist)
    for r in rs:
        if r is s:
            connd,addr = r.accept()
            print("Connect from",addr)
            # 将客户端套接字加入关注列表
            rlist.append(connd)
            with open(r"/home/tarena/test/Net/IO多路复用/log.txt","at") as fa:
                fa.write("客户端地址%s\r\n"%str(r.getsockname()))
        elif r is iput:       # 如果为监控键盘输入事件 追加文本
            with open(r"/home/tarena/test/Net/IO多路复用/log.txt","at") as fa:
                print("CMD")
                fa.write("CMD+"+    iput.readline())
                fa.flush()
        else:
            try:
                data = r.recv(1024)
                r.send(b'ok')
            except:
                rlist.remove(r)
                r.close()
                continue
            print(data.decode())
            with open(r"/home/tarena/test/Net/IO多路复用/log.txt","at") as fa:
                fa.write("时间%s,接收的数据%s\r\n"%(ctime(),data.decode()))
            
                 

    for x in xs:
        pass
