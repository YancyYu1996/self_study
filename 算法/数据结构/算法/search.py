import numpy as np
# 生成一个随机数列表

l = list(np.random.randint(13, size=13))
l2 = list(range(0, 17))


# 顺序查找
def liner(l, n):
    for i in range(len(l)):
        if l[i] == n:
            return i
    else:
        return -1

def binary(l, n):
    mid = len(l)//2
    if n == l[mid]:
        return n
    elif mid == 0:
        return -1
    elif n < l[mid]:
        start = 0
        end = mid
    elif n > l[mid]:
        start = mid
        end = len(l)
    return binary(l[start:end], n)


def binary_02(value, key, left, right):
    if left > right:
        # 查找结束
        return -1

    # 获取中间元素对应下标
    middle = (left + right) // 2
    # 对比中间数据值与待查找值
    if value[middle] == key:
        # 查找成功
        return middle
    elif value[middle] > key:
        # 中间值大于所找的数据
        # 继续在左侧重复该过程
        # 查找范围缩小:左侧不变,右侧变为中间元素的前一位
        return binary_02(value, key, left, middle-1)
    else:
        return binary_02(value, key, middle+1, right)


def binary_03(value, key):
    # 获取左右侧对应下标值
    left = 0
    right = len(value) - 1
    while left <= right:
        # 获取中间数据对应下标值
        middle = (left + right) // 2
        # 比较中间数据与待查找数据
        if value[middle] == key:
            # 查找成功,返回对应下标值
            return middle
        elif value[middle] > key:
            # 继续在左侧重复查找
            # 查找范围缩小:左侧不变,右侧变为中间的前一位
            right = middle - 1
        else:
            # 继续在右侧查找
            left = middle + 1
    # 查找失败,返回-1
    return -1


if __name__ == "__main__":
    print(binary_03(l2, 7))
