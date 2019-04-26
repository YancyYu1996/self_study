from multiprocessing import Process
from time import sleep
import os

def th1():
    sleep(3)
    print("EAT")
    print(os.getppid(),"---",os.getpid())

def th2():
    sleep(2)
    print("sleep")
    print(os.getppid(),"---",os.getpid())

def th3():
    sleep(4)
    print("study python")
    print(os.getppid(),"---",os.getpid())

things=[th1,th2,th3]
process = []
for th in things:
    p = Process(target = th)
    process.append(p)    #使用列表保存进程对象
    p.start()

for _ in process:
    _.join()