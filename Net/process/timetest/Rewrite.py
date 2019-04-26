from multiprocessing import Process
from threading import Thread
#重写进程类  target是传入的函数,args是每个函数传入的参数
class MyProcess(Process):
    def __init__(self,target=(),args ={},kargs={}):  
        self.target = []
        self.args = args
        self.kargs = kargs
        super().__init__()
        for i in target:     
            self.target.append(i)
            if not (i.__name__ in self.args):
                self.args[i.__name__] = ()
            if not (i.__name__ in self.kargs):
                self.kargs[i.__name__] = {}
    def run(self):
        for _ in self.target:
            print(_.__name__)
            _(*(self.args[_.__name__]),**(self.kargs[_.__name__]))

#重写进程类  target是传入的函数,args是每个函数传入的参数
class MyThread(Thread):
    def __init__(self,target=(),args ={},kargs={}):    
        self.target = []
        self.args = args
        self.kargs = kargs
        super().__init__()
        for i in target:          
            self.target.append(i)
            if not (i.__name__ in self.args):
                self.args[i.__name__] = ()
            if not (i.__name__ in self.kargs):
                self.kargs[i.__name__] = {}
    def run(self):
        for _ in self.target:
            print(_.__name__)
            _(*(self.args[_.__name__]),**(self.kargs[_.__name__]))