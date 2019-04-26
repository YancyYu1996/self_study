# tcp_server.py
from socket import *
from server_conf import *
ACCEPT_FLAG = False
class CreateSocket:

    def __init__(self):  
        #创建套接字
        self.sockfd = socket(AF_INET,SOCK_STREAM,0)
        # 绑定地址
        self.sockfd.bind((bindaddr,serverport))
        # 设置监听
        self.sockfd.listen(5) 
    
    def saccept(self):
        # 阻塞等待客户端连接
        print('waiting for connect ....')
        self.connfd,self.addr = self.sockfd.accept()
        print('Connect from',self.addr)   #客户端的地址

    def ResvData(self):
        # 消息接受
        self.data = self.connfd.recv(1024)
        return self.data
    
    def SendData(self,s):
        self.connfd.send(s.encode())
        
    
    def CloseServer(self):    # 关套接字
        self.connfd.close()
    def CloseServerdeep(self):    # 关套接字
        #self.connfd.close()
        self.sockfd.close()




   
    