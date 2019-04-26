# -*- coding:utf-8 -*-
from socket import *
from config import *
import signal
import os,sys

signal.signal(signal.SIGCHLD,signal.SIG_IGN)

def udp_client():
    return socket(AF_INET,SOCK_DGRAM)

def login(s):
    while True:
        name = input("请输入姓名：")
        msg = 'L,' + name     #L表示请求类型
        s.sendto(msg.encode(),client_ADDR)
        # 等待回复
        data,addr = s.recvfrom(1024)
        if data.decode() == "OK":
            print("你已经进入聊天室")
            return name
        else:
            print(data.decode())
def recv_data(s):
    while True:
        data,addr = s.recvfrom(1024)
        if data.decode() == "##":
            break
        print(data.decode()+"\n<<",end = "")
    

def send_data(s,name):
    while True:
        try:
            content = input("<<")
        except KeyboardInterrupt:
            content = "##"
        if content == "##":
            msg = 'Q,' +name     #C表示请求类型
            s.sendto(msg.encode(),client_ADDR)
            sys.exit("退出聊天室")
        
        msg = 'C,' +name+","+ content     #C表示请求类型
        s.sendto(msg.encode(),client_ADDR)

def chat(s,name):
    pid = os.fork()
    if pid < 0:
        print("Create progress Error")
    elif pid == 0:
        send_data(s,name)
        os._exit(0)
    else:
        print("p",os.getpid())
        print("c",pid)
        recv_data(s)
    
def main():
    s = udp_client()
    name = login(s)
    if name:
        chat(s,name)
        
if __name__ =="__main__":
    main()
    
    