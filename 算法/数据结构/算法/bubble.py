def bubble(l):
    for i in range(0,len(l)):
        for j in range(i,len(l)-1):
            if l[j] > l[j+1]:
                l[j],l[j+1] = l[j+1],l[j]
    return l

if __name__ == "__main__":
    s = [1,21,54,12,67,12,78,31,67,100]
    bubble(s)
    print(",".join([str(x) for x in s]))

