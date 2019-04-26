from threading import Thread
from time import ctime
from time import sleep
class MyThread(Thread):
    def __init__(self,target,args=(),kwargs={}):
        super().__init__()
        self.__target = target
        self.__args   = args
        self.__kwargs = kwargs
        
               

    def run(self):
         self.__target(*self.__args,**self.__kwargs)


def player(sec,song):
    for i in range(2):
        print("playing %s:%s"%(song,ctime()))
        sleep(sec)


t = MyThread(target = player,args = (3,),kwargs={"song":"凉凉"})
t.start()
t.join()