# udp_client.py

from socket import *
from server_conf import *

class udp_client:
    def __init__(self):
        # 创建套接字
        self.sockfd = socket(AF_INET,SOCK_DGRAM)
    def SendData(self):
        self.data = input("MAg>>")
        if not self.data:
            return
        self.sockfd.sendto(self.data.encode(),ADDR)
    
    def ResvData(self):
        self.msg,self.addr = self.sockfd.recvfrom(1024)
        print("From server:",self.msg.decode())
    
    def close(self):
        self.sockfd.close()