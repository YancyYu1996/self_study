from multiprocessing import Process
from time import sleep
import signal
#带参数的进程函数
def worker(sec,name):
    for i in range(3):
        sleep(sec)
        print("I am %s"%name)
        print("I am learning")
    
p = Process(target = worker,kwargs = {"name":"yancy","sec":1})

p.start()

signal.signal(signal.SIGCHLD,signal.SIG_IGN)