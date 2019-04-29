#!/usr/bin/env python3.5
from socket import *
import sys
import string
import getpass
HOST = "localhost"
PORT = 11111
ADDR = (HOST,PORT)

s = socket()
# 设置端口立即重用
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, True)
try:
    s.connect(ADDR)
except Exception as e:
    print(e)
    sys.exit()

# 创建网络连接
def main():


    while True:
        print("""
        ============ welcome==================
        ---1.注册         2.登录        3.退出--
        """)
        cmd = input("输入选项:")
        s.send(cmd.encode())
        if cmd not in ['1','2','3']:
            print("请输入正确选项")
        elif cmd == "1":
            do_register()
        elif cmd == "2":
            do_login()
        elif cmd == "3":
            s.send(b'E')
            sys.exit("谢谢使用")

def login(name):
    while True:
        print("""
           =============== Query ==================
           ---1.查单词     2.历史记录       3.注销--
           """)
        cmd = input("输入选项:")
        s.send(cmd.encode())
        if cmd not in ['1', '2', '3']:
            print("请输入正确选项")
        elif cmd == "1":
            do_query(name)
        elif cmd == "2":
            do_hist(name)
        elif cmd == "3":
            return

def do_hist(name):
    msg = "H %s"%name
    s.send(msg.encode())
    data = s.recv(128).decode()
    if data == "OK":
        while True:
            data = s.recv(1024).decode()
            if data == "##":
                break
            print(data)
    else:
        print(data)

def do_query(name):
    while True:
        word = input("单词:")
        if word == "##":
            break
        msg = "Q %s %s"%(name,word)
        s.send(msg.encode())
        # 回复的可能是单词也可能查不到
        data = s.recv(2048).decode()
        print(data)

def do_login():
    name = input("输入姓名:")
    passwd = input("输入密码:")
    msg = "L %s %s"%(name,passwd)
    s.send(msg.encode())
    data = s.recv(128).decode()  # 接受回复
    if data == "OK":
        print("登录成功")
        login(name)
    else:
        print(data)

def do_register():
    while True:
        allChars = string.punctuation + string.whitespace
        # 让用户输入用户名
        while True:
            username = input("请输入用户名:")
            for u in username:
                if u in allChars:
                    print("用户名不合法!!")
                    break
            else:
                break
        passwd_one = input("请输入密码:")
        passwd_two = input("请再次输入密码:")
        if passwd_one == passwd_two:  # 两次密码相同,向服务器发送注册请求
            msg = "R %s %s"%(username,passwd_two)
            # 发送请求
            s.send(msg.encode())
            # 等待回复
            data = s.recv(128).decode()
            if data == "OK":
                print("注册成功")
            else:
                print(data)

            return



if __name__ == '__main__':
    main()