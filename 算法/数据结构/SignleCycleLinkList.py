class Node(object):
    '''节点'''
    def __init__(self, elem):
        self.elem = elem
        self.next = None

class SingleLinkList(object):
    '''单链表'''
    def __init__(self, node = None):
        self.__head = node
        # 如果传了一个node
        if node:
            node.next = node

    def is_empty(self):
        '''链表是否为空'''
        return self.__head is None

    def length(self):
        '''链表长度'''
        if self.is_empty():
            return 0
        # cur游标，用来移动遍历节点
        cur = self.__head
        # count记录数量
        count = 1
        while cur.next != self.__head:
            count += 1
            cur = cur.next
        return count

    def trave(self):
        '''遍历整个链表'''
        if self.is_empty():
            return
        # cur游标，用来移动遍历节点
        cur = self.__head
        while cur.next != self.__head:
            print(cur.elem)
            cur = cur.next
        # 退出循环，cur指向尾节点，但尾节点的值未被打印
        print(cur.elem)

    def add(self,item):
        '''链表头部添加元素'''
        new_node = Node(item)
        if self.is_empty():
            new_node.next = self.__head
            self.__head = new_node
        cur = self.__head
        while cur.next != self.__head:
            cur = cur.next
        new_node.next = self.__head
        self.__head = new_node
        cur.next = new_node

    def append(self,item):
        '''在列表的尾部添加元素'''
        new_node = Node(item)
        if self.is_empty():
            self.__head = new_node
            new_node.next = self.__head
        else:
            # cur游标，用来移动遍历节点
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            cur.next = new_node
            new_node.next = self.__head

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
            prior = self.__head
            # count记录数量
            count = 0
            while count != (pos - 1):
                if count < self.length():
                    count += 1
                    prior = prior.next
            new_node.next = prior.next
            prior.next = new_node

    def remove(self,item):
        '''删除节点'''
        # 如果为空
        if self.is_empty():
            return False
        cur = self.__head
        pre = None
        count = 0
        while cur.next != self.__head:
            if cur.elem == item:
                # 如果查找的是头结点
                if cur == self.__head:
                    # 先找到尾节点
                    while cur.next != self.__head:
                        cur = cur.next
                    cur.next = self.__head.next
                    self.__head = cur.next
                # 如果是中间节点
                else:
                    pre.next = cur.next
                return count
            else:
                count += 1
                pre = cur
                cur = cur.next
        # 退出循环，cur指向尾节点
        if cur.elem == item:
            # 如果只有一个节点
            if cur == self.__head:
                self.__head = None
                return 0
            else:
                pre.next = cur.next
                return count

    def search(self,item):
        '''查找节点是否存在'''
        if self.is_empty():
            return False
        cur = self.__head
        while cur.next != self.__head:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        if cur.elem == item:
            return True
        return False

if __name__ == "__main__":
    new_sll = SingleLinkList()
    print(new_sll.is_empty())
    new_sll.append(2)
    new_sll.trave()
    print(new_sll.remove(2))
    new_sll.trave()