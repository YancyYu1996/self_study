from socket import *
import signal
from config import *
import time
import sys
# 客户端功能类


class FtpClient(object):

    def __init__(self, sockfd):
        self.sockfd = sockfd

    def do_list(self):
        self.sockfd.send(b'L')  # 发送请求
        # 等待回复
        data = self.sockfd.recv(128).decode()
        if data == "ok":
            file_list = self.sockfd.recv(4096).decode()
            for file in file_list.split("*"):
                print(file)
            
        else:
            # 无法完成操作
            print(data)

    def do_quit(self):
        self.sockfd.send(b'Q')
        self.sockfd.close()
        sys.exit("谢谢使用")

    def get_file(self, filename):
        self.sockfd.send(("G*"+filename).encode())
        data = self.sockfd.recv(128).decode()
        if data == "ok":
            fw = open(SAVE_PATH, 'wb')
            while True:
                data = self.sockfd.recv(1024)
                if data == b'##':
                    break
                fw.write(data)
        else:
            print(data)

    def put_file(self, filename):
        self.sockfd.send(("P*"+filename).encode())
        data = self.sockfd.recv(128).decode()
        if data == "ok":
            try:
                fr = open(SAVE_PATH+filename, 'rb')
            except IOError:
                print("文件不存在")
                return

            while True:
                data = fr.read(1024)
                if not data:
                    time.sleep(0.1)
                    self.sockfd.send(b'##')
                    print("上传完成")
                    fr.close()
                    break
                self.sockfd.send(data)
        else:
            print(data)


def print_menu():
    print('\n============命令选项==============')
    print("***************1.显示***************")   
    print("***************2.上传***************")  
    print("***************3.下载***************")
    print("***************4.退出***************")
    print("====================================")


def main():
    # 创建套接字
    sockfd = socket()
    # 发起连接
    server_addr = ('localhost', PORT)
    signal.signal(signal.SIGCHLD, signal.SIG_IGN)

    try:
        sockfd.connect(server_addr)
    except Exception as e:
        print(e)
        return      
    # 创建对象,调用功能函数
    ftp = FtpClient(sockfd)
    while True:   
        
        print_menu()
        cmd = input("输入命令>>")
        if cmd.strip() == "1":
            ftp.do_list()
        elif cmd.strip() == "q":
            ftp.do_quit()
        elif cmd.strip() == "3":
            cmd = input("输入获取文件指令>>")
            filename = cmd.strip().split(" ")[-1]
            ftp.get_file(filename)
        elif cmd.strip() == "2":
            file_list = os.listdir(SAVE_PATH)
            if not file_list:
                print("文件库为空")
                continue
            else:
                for file in file_list:
                    if file[0] != "." and os.path.isfile(SAVE_PATH+file):
                        print(file) 
                cmd = input("输入上传指令>>")
                filename = cmd.strip().split(" ")[-1]
                ftp.put_file(filename)
        else:
            print("请输入正确的选项")
            

if __name__ == "__main__":
    main()
