# 快速排序
# 递归

def quickly(alist):
    if len(alist) < 2:
        return alist

    # 获取关键数据
    mark = alist[0]
    smaller = [x for x in alist if x < mark]
    # 找出所有关键数据大的
    bigger = [x for x in alist if x > mark]

    # 找出所有与关键数据相等的
    eq = [x for x in alist if x == mark]

    # 从小到达排列
    return quickly(smaller) + eq + quickly(bigger)

l = [1,5,2,76,23,89,23,87,100,90]
if __name__ == "__main__":
    val = quickly(l)
    print(",".join([str(x) for x in val]))

