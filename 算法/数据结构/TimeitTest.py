#1.代码执行时间测量模块timeit
#2.python列表类型不同
from timeit import Timer

l1 = [1,2]
l2 = [3,4]
li = l1 + l2
li = [i for i in range(10000)]
li = list(range(10000))



def test1():
    li = []
    for i in range(10000):
        li.append(i)

def test2():
    li = []
    for i in range(10000):
        li += [i]

def test3():
    li = [i for i in range(10000)]

def test4():
    li = list(range(10000))

def test5():
    li = []
    for i in range(10000):
        li.extend([i])


timer1 = Timer("test1()","from __main__ import test1")
print("append:",timer1.timeit(1000))
timer2 = Timer("test2()","from __main__ import test2")
print("+=:",timer2.timeit(1000))
timer3 = Timer("test3()","from __main__ import test3")
print("[i fro i in range]:",timer3.timeit(1000))
timer4 = Timer("test4()","from __main__ import test4")
print("list(range()):",timer4.timeit(1000))
timer5 = Timer("test5()","from __main__ import test5")
print("li.extend:",timer5.timeit(1000))

def t6():
    li = []
    for i in range(10000):
        li.append(i)

def t7():
    li = []
    for i in range(10000):
        li.insert(0,i)
    print(li)
