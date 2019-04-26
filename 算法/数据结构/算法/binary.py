l = [1,2,4,7,23,54]
def binary_search(alist,item):
    """二分法查找"""
    n = len(alist)
    if n == 0:
        return False
    mid = n//2
    if alist[mid] == item:
        return item
    elif item < alist[mid]:
        binary_search(alist[:mid],item)
    else:
        binary_search(alist[mid+1:],item)

print(binary_search(l,5))
