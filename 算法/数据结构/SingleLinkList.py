class Node(object):
    '''节点'''
    def __init__(self, elem):
        self.elem = elem
        self.next = None

class SingleLinkList(object):
    '''单链表'''
    def __init__(self, node = None):
        self._head = node

    def is_empty(self):
        '''链表是否为空'''
        return self._head is None

    def length(self):
        '''链表长度'''
        # cur游标，用来移动遍历节点
        cur = self._head
        # count记录数量
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def trave(self):
        '''遍历整个链表'''
        # cur游标，用来移动遍历节点
        cur = self._head
        while cur != None:
            print(cur.elem)
            cur = cur.next

    def add(self,item):
        '''链表头部添加元素'''
        new_node = Node(item)
        new_node.next = self._head
        self._head = new_node

    def append(self,item):
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
            prior = self._head
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
        cur = self._head
        pre = None
        count = 0
        while cur != None:
            if cur.elem == item:
                if cur == self._head:
                    self._head = cur.next
                else:
                    pre.next = cur.next
                return count
            else:
                count += 1
                pre = cur
                cur = cur.next


    def search(self,item):
        '''查找节点是否存在'''
        cur = self._head
        while cur != None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False

if __name__ == "__main__":
    new_sll = SingleLinkList()
    print(new_sll.is_empty())
    new_sll.append(2)
    new_sll.append(5)
    new_sll.append(7)
    new_sll.add(1)
    new_sll.insert(65, 76)
    new_sll.trave()
    print(new_sll.remove(5))
    new_sll.trave()