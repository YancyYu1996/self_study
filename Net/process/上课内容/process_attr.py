from multiprocessing import Process
from time import sleep,ctime

def fun():
    for i in range(3):
        sleep(2)
        print(ctime())

p = Process(target = fun)
p.daemon = True
p.start()
print("name：",p.name)
print("PID：",p.pid)
print("Alive：",p.is_alive()) 