# -*- coding:utf-8 -*-
"""
Chat room server
env:python3.52
exc:for socket and fork
"""
from socket import *
from config import *
import os,sys
from select import  select
# 存储用户信息的字典
user = {}

iput = sys.stdin
#添加到关注列表
rlist = [iput]
wlist = []
xlist = []

# 搭建网络连接
def udp_server():
    # 创建套接字
    s = socket(AF_INET,SOCK_DGRAM)
    s.bind(server_ADDR)
    return s

def do_login(s,name,addr):
    if name in user:
        s.sendto("该用户已经存在".encode(),addr)
        return
    else:
        s.sendto(b"OK",addr)

        #通知其他人
        msg = "欢迎 %s 进入聊天室"%name
        for i in user:
            s.sendto(msg.encode(),user[i])
        #加入字典
        user[name] = addr
def chat(s,name,content):
    msg = "%s:%s"%(name,content)
    for i in user:
        if i != name:
            s.sendto(msg.encode(),user[i])

def quit_room(s,name):
    msg = "%s退出聊天室"%name
    s.sendto(b'##',user[name])
    user.pop(name)
    for i in user:
        s.sendto(msg.encode(),user[i])
    

def send_notice(s,notice_msg):
    msg = "最新公告：\n"+notice_msg
    for i in user:
        s.sendto(msg.encode(),user[i])   


def request(s):
    while True:
        # 监控IO
        rs,ws,xs = select(rlist,wlist,xlist)
        for _ in rs:
            if _ is s:
                data,addr = s.recvfrom(1024)
                msglist = data.decode().split(",")
                # 区分请求类型
                if msglist[0] == "L":
                    do_login(s,msglist[1],addr)
                elif msglist[0] == "C":
                    chat(s,msglist[1],msglist[2])
                elif msglist[0] == "Q":
                    quit_room(s,msglist[1])
            elif _ is iput:
                send_notice(s,iput.readline())
                
def main():
    s = udp_server()
    rlist.append(s)
    
    request(s)



if __name__ == "__main__":
    main()