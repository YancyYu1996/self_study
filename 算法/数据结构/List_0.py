#队列 先进先出
#操作
#Queue()        创建一个新队列
#enqueue(item)  往队列中添加一个item元素
#dequeue()      从队列头部弹出取出一个元素
# is_empty()    判断一个的队列是否为空
# size()        返回队列的大小
class Queue():
    def __init__(self):
        self.__list = []
    def enqueue(self,item):
        '''往队列中添加一个item元素'''
        self.__list.append(item)

    def dequeue(self):
        '''从队列头部弹出取出一个元素'''
        return self.__list.pop(0)

    def is_empty(self):
        '''判断一个的队列是否为空'''
        return self.__list == []

    def size(self):
        '''返回队列的大小'''
        return len(self.__list)

#操作
#Deque()        创建一个空的双端队列
#add_front(item)  往队列头部中添加一个item元素
#add_rear(item)   往队列尾部中添加一个item元素
#remove_front()   从队列头部删除一个item元素
#remove_rear()   从队列尾部删除一个item元素
# is_empty()    判断一个的队列是否为空
# size()        返回队列的大小


class Deque():
    def __init__(self):
        self.__list = []
    def add_front(self,item):
        '''往队列头部中添加一个item元素'''
        self.__list.insert(0,item)

    def add_rear(self,item):
        '''往队列尾部中添加一个item元素'''
        self.__list.append(item)

    def remove_front(self):
        '''往从队列头部删除一个item元素'''
        return self.__list.pop(0)

    def remove_rear(self):
        '''从队列尾部删除一个item元素'''
        return self.__list.pop()

    def is_empty(self):
        '''判断一个的队列是否为空'''
        return self.__list == []

    def size(self):
        '''返回队列的大小'''
        return len(self.__list)


if __name__ == "__main__":
    s = Queue()
    s.enqueue(1)
    s.enqueue(3)
    s.enqueue(4)
    s.enqueue(5)

    print(s.dequeue())
    print(s.dequeue())
    print(s.dequeue())
    print(s.dequeue())

