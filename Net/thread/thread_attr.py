from threading import Thread
from time import sleep

def fun():
    sleep(1)
    print("Thread Test")

t = Thread(target=fun,name = "YANCY")

# 线程名称
t.setName("bb")
print("Thread name:",t.getName())

# 设置daemon值
t.setDaemon(True)

t.start()
print("is alive",t.is_alive())
