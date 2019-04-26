"""
通过socketserver模块完成网络并发
"""

from socketserver import *


# 创建一个tcp多进程并发
class Server(ForkingMixIn, TCPServer):
    pass


# 具体的请求处理类
class Handle(StreamRequestHandler):
    # 重写处理方法
    def handle(self):
        print("connect from:",self.client_address)
        while True:
            # self.request ==> accept -> connfd
            data = self.request.resv(1024)
            if not data:
                break
            print(data.decode())
            self.request.send(b'OK')

# 创建服务器对象
serv = Server(('0.0.0.0',1111),Handle)
serv.serve_forever()   # 启动服务
