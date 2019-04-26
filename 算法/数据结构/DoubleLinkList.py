# coding:utf-8
from SingleLinkList import *

class Node(object):
    '''结点'''
    def __init__(self, item):
        self.elem = item
        self.next = None
        self.prev = None


class DoubleLinkList(SingleLinkList):
    '''双链表'''
    def __init__(self, node = None):
        self._head = node

    def add(self, item):
        '''链表头部添加元素'''
        new_node = Node(item)
        new_node.next = self._head
        self._head = new_node
        new_node.prev = new_node

    def append(self, item):
        '''在列表的尾部添加元素'''
        new_node = Node(item)
        if self.is_empty():
            self._head = new_node
        else:
            # cur游标，用来移动遍历节点
            cur = self._head
            while cur.next != None:
                cur = cur.next
            cur.next = new_node
            new_node.prev = cur

    def insert(self, pos, item):
        '''指定位置添加元素
        :param pos 从0开始
        '''
        if pos <= 0:
            self.add(item)
        elif pos > self.length():
            self.append(item)
        else:
            new_node = Node(item)
            # cur游标，用来移动遍历节点
            cur = self._head
            # count记录数量
            count = 0
            while count != pos:
                if count < self.length():
                    count += 1
                    cur = cur.next
            new_node.next = cur
            new_node.prev = cur.prev
            cur.prev.next = new_node
            cur.prev = new_node

    def remove(self,item):
        '''删除节点'''
        cur = self._head
        count = 0
        while cur != None:
            if cur.elem == item:
                # 如果是第一个节点
                if cur == self._head:
                    self._head = cur.next
                    # 如果不是只有一个节点
                    if cur.next:
                        cur.next.prev = None
                else:
                    cur.prev.next = cur.next
                    if cur.next != None:
                        cur.next.prev = cur.prev
                return count
            else:
                count += 1
                cur = cur.next


if __name__ == "__main__":
    new_sll = DoubleLinkList()
    print(new_sll.is_empty())
    new_sll.append(2)
    new_sll.append(5)
    new_sll.append(7)
    new_sll.add(1)
    new_sll.insert(65, 76)
    new_sll.trave()

    print(new_sll.remove(76))
    new_sll.trave()