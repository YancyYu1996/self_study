from threading import Thread,Event
from time import sleep

s = None
e = Event() # 创建event对象
def 垃圾():
    sleep(1)
    print("shit")
    global s
    s = "智障"
    e.set()

f = Thread(target=垃圾)
f.start()

#严重口令
print("say")
e.wait()# 添加阻塞
if s == "智障":
    print("yes")
else:
    print("kiss my ass")

f.join()