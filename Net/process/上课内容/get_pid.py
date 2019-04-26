import os
from time import sleep

pid = os.fork()
if pid < 0:
    print("Error")
elif pid == 0:
    sleep(2)
    print("Child PID",os.getpid())
    print("get Parents PID",os.getppid())
else:
    print("get Child PID",pid)
    print("Parents PID",os.getpid())