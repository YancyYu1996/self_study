import threading
from time import sleep
import os
a = 1
# 线程函数
def music():
    global a
    a = 1000
    for i in range(5):
        sleep(1)
        print("命运交响曲",os.getpid())

# 创建线程对象
t = threading.Thread(target=music)
t.start()

# 主线程执行
for i in range(3):
    sleep(1)
    print("sunny",os.getpid())

t.join()
print(a)