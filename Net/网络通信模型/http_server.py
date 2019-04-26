"""
HTTP Server 2.0
"""

from socket import *
from threading import Thread
import sys


# 封装HTTP类做一个完整的服务功能
class HTTPServer(object):
    def __init__(self, server_address, statit_dir):
        # 属性添加
        self.server_address = server_address
        self.statit_dir = statit_dir
        self.sockfd = None
        self.ip = server_address[0]
        self.port = server_address[1]
        self.create_socket()
        self.bind()

    # 创建套接字
    def create_socket(self):
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    def bind(self):
        self.sockfd.bind(self.server_address)

    def server_forever(self):
        self.sockfd.listen(5)
        print("Listen the port %d" % self.port)
        while True:
            try:
                connfd, addr = self.sockfd.accept()
            except KeyboardInterrupt:
                self.sockfd.close()
                sys.exit("退出服务器")
            except Exception as e:
                print(e)
                continue
            # 创建新的线程处理请求
            th = Thread(target=self.handle, args=(connfd,))
            th.setDaemon(True)
            th.start()

    def handle(self, connfd):
        # 接收http请求
        request = connfd.recv(4096)
        if not request:
            return
        # 请求解析
        requestHeaders = request.splitlines()
        print(connfd.getpeername(), ":", requestHeaders[0])
        getRequest = requestHeaders[0].decode().split(' ')[1]
        if getRequest == '/' or getRequest[-5:] == ".html":
            self.get_html(connfd, getRequest)
        else:
            self.get_data(connfd)
        connfd.close()

    def get_html(self, connfd, getRequest):
        if getRequest == "/":
            filename = self.statit_dir + "/index.html"
        else:
            filename = self.statit_dir + getRequest
        print(getRequest)
        print(filename)
        try:
            f = open(filename)
        except IOError:
            # 没有这个网页
            responseHeaders = 'HTTP/1.1 404 Not Found\r\n'
            responseHeaders += "\r\n"
            responseBody = "Sorry Not Found the page"

        else:
            responseHeaders = 'HTTP/1.1 200 Ok\r\n'
            responseHeaders += "\r\n"
            responseBody = f.read()
        finally:
            response = responseHeaders + responseBody
            connfd.send(response.encode())

    def get_data(self,connfd):
        data = """HTTP/1.1 200 OK\r\n\r\n<p>Waiting httpserver v3.0</p>"""
        connfd.send(data.encode())

if __name__ == "__main__":
    # 使用者想用http类干什么
    # 启动服务,用于展示我的一些静态网页
    # 什么需要用户提供
    # 服务端地址和网页
    # 用户怎么用这么类
    # 服务地址
    server_addr = ("0.0.0.0", 8000)
    # 网页存放地址
    statis_dir = '/home/tarena/test/Net/网络通信模型/static'
    # 生成服务器对象
    httpd = HTTPServer(server_addr, statis_dir)
    # 启动服务
    httpd.server_forever()
