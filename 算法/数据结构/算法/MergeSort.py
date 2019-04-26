# coding:utf-8
l = [1,2,4,6,8,56,54,12]

def merge_sort(alist):
    '''归并排序'''
    n = len(alist)
    if n <= 1:
        return alist
    mid = n//2
    # left 采用归并排序后形成的有序的新的列表
    left_li = merge_sort(alist[:mid])
    # right 采用归并排序后形成的有序的新的列表
    right_li = merge_sort(alist[mid:])
    # 将两个有序的子序列合并为一个新的整体
    left_p, right_p = 0, 0
    result = []
    while (left_p < len(left_li)) and \
            (right_p < len(right_li)):
        if left_li[left_p] < right_li[right_p]:
            result.append(left_li[left_p])
            left_p += 1
        else:
            result.append(right_li[right_p])
            right_p += 1
    result += left_li[left_p:]
    result += right_li[right_p:]
    return result


print(",".join([str(x) for x in l]))
a = merge_sort(l)
print(a)
