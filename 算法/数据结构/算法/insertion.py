# 前面有序 将后面的数字插入前面有序数列合适的位置
import numpy as np
l = np.random.randint(0,100,13)
def insertion(l):
    for i in range(len(l)-1):
        for j in range(i+1,0,-1):
            if (l[j-1] > l[j]):
                l[j-1],l[j] = l[j],l[j-1]
            else:
                continue
    return l

print(",".join([str(x) for x in l]))
print(",".join([str(x) for x in insertion(l)]))

