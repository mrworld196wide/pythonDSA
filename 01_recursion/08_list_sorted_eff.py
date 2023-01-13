def isSortedBetter(a,si):
    l = len(a)
    if si == l-1 or si == l:
        return True

    if a[si] > a[si+1]:
        return False
    isSmallerPartSorted = isSortedBetter(a, si + 1)
    return isSmallerPartSorted
    
a = [1,22,3,5,6,7,8,9]
isSortedBetter(a, 3)
 