# 选择排序，前面有序，选择后面最小的值插入前面
import numpy as np
l = np.random.randint(0,100,13)

def choose(l):
    for _ in range(len(l)):
        for j in range(_,len(l)):
            if l[j] < l[_]:
                l[j], l[_] = l[_], l[j]
            else:
                continue
    return l


print(",".join([str(x) for x in l]))
print(",".join([str(x) for x in choose(l)]))
