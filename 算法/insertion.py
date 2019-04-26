def insertion(l):
    for i in range(len(l)):
        flag = l[i]
        for j in range(1,l):
            if (flag > l[j-1]) and (flag < l[j]):
                flag = l[j]
