import gevent

def foo(a, b):
    print("Runing foo", a, b)
    gevent.sleep(3)
    print("Foo over")

def bar():
    print("Runing bar")
    gevent.sleep(2)
    print("bar over")

f = gevent.spawn(foo, 1, 2)
b = gevent.spawn(bar)
gevent.joinall([f,b])