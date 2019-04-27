'''
Aid httpserver v3.0
'''

from socket import *
import sys
from threading import Thread
from config import *
import re
import json

# 服务器地址
ADDR = (HOST,PORT)

# 和webFrame通信
def connect_frame(env):
    s = socket()
    try:
        s.connect((frame_ip,frame_port)) # 连接webframe
    except Exception as e:
        print(e)
        return
    else:
        # 将请求字典转换为json数据发送
        data = json.dumps(env)
        s.send(data.encode())
        # 接收webframe数据
        data = s.recv(4096*100).decode()
        return json.loads(data) # 返回数据字典


# 封装httpserver基本功能
class HTTPServer(object):
    def __init__(self,addr):
        self.address = addr
        self.create_socket()
        self.bind()

    def create_socket(self):
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,DEBUG)

    # 绑定地址
    def bind(self):
        self.sockfd.bind(self.address)
        self.ip = self.address[0]
        self.port = self.address[1]

    # 启动服务器
    def server_forever(self):
        self.sockfd.listen(5)
        print("Listen the port %d..."%self.port)
        while True:
            connfd,addr = self.sockfd.accept()
            print("Connect from",addr)
            client = Thread(target=self.handle,\
                            args=(connfd,))
            client.setDaemon(True)
            client.start()

    def handle(self,connfd):
        request = connfd.recv(4096).decode()
        pattern = r"(?P<method>[A-Z]+)\s+(?P<info>/\s*)"
        try:
            # env = request
            env = re.match(pattern,request).groupdict()
        except:
            print("error")
            connfd.close()
            return
        else:
            print(env)
            data = connect_frame(env)
            if data:
                self.response(connfd,data)

    # 将数据整理为响应格式发送给浏览器
    def response(self,connfd,data):
        # data {'status':"200",data:"content"}
        if data['status'] == "200":
            responseHeaders = "HTTP/1.1 200 OK\r\n"
            responseHeaders += "Content-Type:text/html\r\n"
            responseHeaders += "\r\n"
            responseBody = data['data']

        elif data['status'] == "404":
            responseHeaders = "HTTP/1.1 404 Error\r\n"
            responseHeaders += "Content-Type:text/html\r\n"
            responseHeaders += "\r\n"
            responseBody = data['data']
        elif data['status'] == "500":
            pass

        # 将数据发送给浏览器
        response_data = responseHeaders + responseBody
        connfd.send(response_data.encode())




if __name__ == '__main__':
    httpd = HTTPServer(ADDR)
    httpd.server_forever()