# coding:utf-8
import numpy as np
l = np.random.randint(0,100,13)
def shell_sort(alist):
    '''希尔排序'''
    n = len(alist)
    gap = n//2
    while gap > 0:
        # 插入算法与普通插入算法的区别就是gap步长
        for x in range(gap, n):
            _ = x
            while _ >0:
                if alist[_] < alist[_-gap]:
                    alist[_],alist[_-gap] = alist[_-gap],alist[_]
                    _ -= gap
                else:
                    break
        gap //= 2
    return alist

print(",".join([str(x) for x in l]))
print(",".join([str(x) for x in shell_sort(l)]))