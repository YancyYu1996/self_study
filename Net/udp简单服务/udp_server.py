# udp_server.py
from socket import *

class udp_server:
    def __init__(self):
        # 创建数据报套接字
        self.sockfd = socket(AF_INET,SOCK_DGRAM)
        # 绑定地址
        self.server_addr = ('0.0.0.0',8888)
        self.sockfd.bind(self.server_addr)
        print("connect")
    #收发消息
    def ResvData(self):
        self.data,self.addr = self.sockfd.recvfrom(1024)
        print("Receve from %s:%s"%(self.addr,self.data.decode()))
    
    def SendData(self):
        self.sockfd.sendto(b'Thanks for your msg',self.addr)
   
    # 关闭套接字
    def close(self):
        self.sockfd.close()

    
    
    


