# 快速排序
# 递归

def quickly(l):
    if len(l) < 2:
        return l

    # 获取关键数据
    mark = l[0]
    smaller = [x for x in l if x < mark]
    # 找出所有关键数据大的
    bigger = [x for x in l if x < mark]

    # 找出所有与关键数据相等的
    eq = [x for x in l if x == mark]

    # 从小到达排列
    return quickly(smaller) + bigger + quickly(eq)

l = [1,5,2,76,23,89,23,87.100,90]
if __name__ == "__main__":
    vaule = quickly(l)
    print(vaule)

