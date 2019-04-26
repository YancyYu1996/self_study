# queue_0.py
from multiprocessing import Queue,Process
from time import sleep

# 创建消息队列
q = Queue(5)
def createQueue():
    for i in range(5):
        q.put(("send",i))


def resv_msg():
    for i in range(6):
        try:
            a,b = q.get(timeout = 2)
        except:
            return
        print("%s,%d"%(a,b))

p1 = Process(target = createQueue)
p2 = Process(target = resv_msg)

p1.start()
p2.start()
p1.join()
p2.join()
