import os
from time import sleep

pid = os.fork()

if pid == 0:
    print("child process",os.getpid())
    os._exit(0)
else:
    print("parent process,yancy")
    while True:
        pass