import select
from socket import *

fr = open(r"E:\python_Class\ubantu_code\Net\套接字\resv.bmp")
#创建套接字作为关注的IO
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',8000))
s.listen(5)

#添加到关注列表
rlist = [s]
wlist = []
xlist = [fr]
print("开始监控IO")
rs,ws,xs = select.select(rlist,wlist,xlist)