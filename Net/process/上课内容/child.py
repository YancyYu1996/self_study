import os
from time import sleep

def f1():
    sleep(2)
    print("yancy study")

def f2():
    print("yancy eat")

def f3():
    sleep(2)
    print("yancy sleep")

pid = os.fork()

if pid < 0:
    print("Error")
elif pid == 0:
    p = os.fork()
    if p == 0:
        f1()
    else:
        os._exit(0)
else:
    os.wait()
    f3()    