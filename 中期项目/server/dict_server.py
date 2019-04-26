#!/usr/bin/env python3.5
from socket import  *
import  pymysql
import os,sys
import time
import signal

# 全局变量
if len(sys.argv) < 3:
    print('''Run server as:
    python3 dict_server.py 0.0.0.0 1111
    ''')
    sys.exit()

HOST = sys.argv[1]
PORT = int(sys.argv[2])
ADDR = (HOST,PORT)
DICT_TEXT = "../dict.txt"
def do_request(c,db):
    while True:
        # 接受客户端请求
        data = c.recv(1024).decode()
        print(c.getpeername(),':',data)
        if not data or data == "E":
            return
        if data[0] == "R":
            do_register(c,db,data)
        elif data[0] == "L":
            do_login(c,db,data)
        elif data[0] == "Q":
            do_query(c,db,data)
        elif data[0] == "H":
            do_hist(c,db,data)

def do_hist(c,db,data):
    tmp = data.split(" ")
    name = tmp[1]
    cursor = db.cursor()

    sql = "select * from hist where name = '%s' order by id desc limit 10"%name
    cursor.execute(sql)
    r = cursor.fetchall()
    if not r:
        c.send("无查询记录".encode())
        return
    c.send(b'OK')
    for i in r:
        msg = "%s   %s    %s"%(i[1],i[2],i[3])
        time.sleep(0.1)
        c.send(msg.encode())
    time.sleep(0.1)
    c.send(b'##')

def do_query(c,db,data):
    tmp = data.split(" ")
    name = tmp[1]
    word = tmp[2]

    # 插入历史记录
    cursor = db.cursor()
    tm = time.ctime()
    sql = "insert into hist (name,word,time) values ('%s','%s','%s')"\
    %(name,word,tm)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    # 数据库查询
    cursor = db.cursor()
    sql = "select mean from words where word = '%s'"%word
    cursor.execute(sql)
    r = cursor.fetchone()
    if r:
        c.send(r.encode())
    else:
        c.send("没有找到单词".encode())

    # # 文本查询
    # f = open(DICT_TEXT)
    # for line in f:
    #     w = line.split(" ")[0]
    #     if w > word:
    #         break
    #     elif w == word:
    #         c.send(line.encode())
    #         f.close()
    #         return
    #
    # c.send("没有找到该单词".encode())

def do_login(c,db,data):
    tmp = data.split(" ")
    name = tmp[1]
    passwd = tmp[2]
    cursor = db.cursor()

    sql = "select * from user where name = '%s' and passwd = '%s'"\
    %(name,passwd)
    cursor.execute(sql)
    r = cursor.fetchone()
    if r:
        c.send(b'OK')
    else:
        c.send("登录失败".encode())

# 搭建网络连接
def main():
    # 连接数据库
    db_conn = pymysql.connect(
        '127.0.0.1',
        'yancy',
        'yancy1996',
        'Dictoray',
        charset = 'utf8'
    )

    # 创建套接字
    s = socket()
    # 设置端口立即重用
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, True)
    s.bind(ADDR)
    s.listen(5)

    # 处理僵尸进程
    signal.signal(signal.SIGCHLD,signal.SIG_IGN)

    while True:
        try:
            c,addr = s.accept()
            print("Connect from",addr)
        except KeyboardInterrupt:
            s.close()
            sys.exit("服务器退出")
        except Exception as e:
            print(e)
            continue
        # 创建子进程
        pid = os.fork()
        if pid == 0:
            s.close()
            do_request(c,db_conn)  # 处理客户端请求
            sys.exit()
        else:
            c.close()

def do_register(c,db,data):
        tmp = data.split(" ")
        name = tmp[1]
        passwd = tmp[2]
        cursor = db.cursor()

        sql = "select * from user where name = '%s'"% name
        cursor.execute(sql)
        r = cursor.fetchone()
        if r != None:
            c.send('该用户已存在'.encode())
            return
        else:
            sql = "insert into user (name,passwd) values \
('%s','%s')"%(name,passwd)
            try:
                cursor.execute(sql)
                db.commit()
                c.send(b'OK')
            except:
                db.rollback()
                c.send("注册失败".encode())



if __name__ == '__main__':
    main()