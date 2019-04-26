# 重要

from socket import *
import os,sys
import signal
from config import *
import time

# 处理僵尸进程

# 服务端功能类
class FtpServer(object):
    def __init__(self,connfd):
        self.connfd = connfd
    def do_list(self):
        # 或许文件列表
        file_list = os.listdir(FILE_PATH)
        if not file_list:
            self.connfd.send("文件库为空".encode())
            return
        else:
            self.connfd.send(b'ok')
            time.sleep(0.1)
            files = ""
            for file in file_list:
                if file[0] != "." and os.path.isfile(FILE_PATH+file):
                    files += file + "*"
            print(files)
            self.connfd.send(files.encode())
        
    def do_get(self,filename):
        try:
            fd = open(FILE_PATH+filename,'rb')
        except IOError as e:
            self.connfd.send("文件不存在".encode())
            return
        else:
            self.connfd.send(b"ok")
            time.sleep(0.1)
        # 发送文件内容
        while True:
            data = fd.read(1024)
            if not data:
                time.sleep(0.1)
                self.connfd.send(b"##")
                break
            self.connfd.send(data)
        fd.close()
    def do_put(self,filename):
        if os.path.exists(FILE_PATH+filename):
            self.connfd.send("文件已经存在".encode())
            return
        else:
            self.connfd.send(b"ok")
            time.sleep(0.1)
            fa = open(FILE_PATH+filename,'ab')
            # 接受文件内容
            while True:
                data = self.connfd.recv(1024)
                if data == b'##':
                    break
                fa.write(data)
            fa.close()

def client_handle(connfd):
    ftp = FtpServer(connfd)
    while True:
        data = connfd.recv(1024).decode()
        if not data or data[0] == "Q":
            connfd.close()
            print("客户端退出")
            return
        elif data[0] == 'L':
            ftp.do_list()
        elif data[0] == 'G':
            filename = data.split('*')[-1]
            ftp.do_get(filename)
        elif data[0] == "P":
            filename = data.split('*')[-1]
            ftp.do_put(filename)


        
    
    connfd.close()


def main():
    s = socket()
    # 立即重用
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind(ADDR)
    s.listen(5)
    signal.signal(signal.SIGCHLD,signal.SIG_IGN)
    print("listen the port 1111...")
    # 循环等待客户端连接
    while True:
        try:
            c,addr = s.accept()
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
            client_handle(c)    # 处理客户端请求
            os._exit(0)
        else:
            c.close()



if __name__ == "__main__":
    main()

