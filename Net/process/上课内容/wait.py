import os 
from time import sleep

pid = os.fork()

if pid <0:
    print("Error")
elif pid == 0:
    sleep(3)
    cpid = os.fork()
    print("child %d process exit"%(os.getpid()))
    os._exit(2)
else:
    pid,status = os.wait()
    print("pid:",pid)
    print("status",os.WEXITSTATUS(status))
    while True:
        sleep(100)