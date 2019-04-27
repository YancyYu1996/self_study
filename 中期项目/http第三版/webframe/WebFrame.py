'''
模拟网站后端应用程序工作
'''
from socket import *
import json
from setting import *
from select import select

frame_address = (frame_ip,frame_port)
# 应用类,将功能封装在类中
class Application(object):
    def __init__(self):
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,DEBUG)
        self.sockfd.bind(frame_address)

    def start(self):
        self.sockfd.listen(5)
        print("Linsten the port %d"%frame_port)
        rlist = [self.sockfd]
        wlist = []
        xlist = []
        # select IO多路复用监听请求
        while True:
            rs,ws,xs = select(rlist,wlist,xlist)
            for r in rs:
                if r is self.sockfd:
                    connfd,addr = r.accept()
                    rlist.append(connfd)
                else:
                    self.handle(r)
                    # rlist.remove(r)

    def handle(self,connfd):
        request = connfd.recv(1024).decode()
        request = json.loads(request) # 请求字典
        if request['method'] == "GET":
            if request['info'] == "/" or request['info'][-5:]=='.html':
                response = self.get_html(request['info'])
            else:
                response = self.get_data(request["info"])

        elif request['method'] == "POST":
            pass

        # 将数据发送给httpserver
        response = json.dumps(response)
        connfd.send(response.encode())
        connfd.close()

    # 处理网页
    def get_html(self,info):
        if info == '/':
            filename = STATIC_DIR + "/index.html"
        else:
            filename = STATIC_DIR + info
        try:
            fd = open(filename)
        except IOError:
            with open(STATIC_DIR+"/error.html") as f:
                data = f.read()
            return {"status":'404','data':data}
        else:
            return {"status":'200','data':fd.read()}


    def get_data(self,info):
        pass



if __name__ == '__main__':
    app = Application()
    app.start()