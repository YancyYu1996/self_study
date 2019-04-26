
from timeit import Timer
from Rewrite import MyProcess,MyThread
from multiprocessing import Process
from threading import Thread
# 计算密集

def count(x,y):
    c = 0 
    while c < 7000000:
        x += 1
        y += 1
        c += 1 
# IO密集
def io():
    write()
    read()

def write():
    f = open('test','w')
    for i in range(1700000):
        f.write("hello world\n")

def read():
    f = open('test')
    f.readlines()
    f.close()


# 自定义传参方式
#函数的名称
ptarget = (count,io,write,read)   
#函数的位置传参
pargs = {"count":(10,)} 
# 函数的关键字传参 
pkargs = {"count":{"y":10}}  
p = MyProcess(target =ptarget,args=pargs, kargs=pkargs)

t = MyThread(target =ptarget,args=pargs, kargs=pkargs)

p1 = Process(target =count,args=(10,10))
p2 = Process(target =io)
p3 = Process(target =write)
p4 = Process(target =read)

t1 = Thread(target =count,args=(10,10))
t2 = Thread(target =io)
t3 = Thread(target =write)
t4 = Thread(target =read)
def ptest():
    p.start()
    p.join()

def ptest2():
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p1.join()
    p2.join()
    p3.join()
    p4.join()
def ttest():
    t.start()
    t.join()
def ttest2():
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()

def testall():
    count(10,10)
    io()
    write()
    read()

tim1 = Timer("count(1,1)", "from __main__ import count")
print("count ",tim1.timeit(number=10), "seconds")
# tim2 = Timer("ptest2()", "from __main__ import ptest2")
# print("ptest2 ",tim2.timeit(number=1), "seconds")

# tim3 = Timer("ttest()", "from __main__ import ttest")
# print("ttest ",tim3.timeit(number=1), "seconds")

# tim4 = Timer("ttest2()", "from __main__ import ttest2")
# print("ttest2 ",tim4.timeit(number=1), "seconds")

# tim5 = Timer("testall()", "from __main__ import testall")
# print("testall ",tim5.timeit(number=1), "seconds")


            

        


