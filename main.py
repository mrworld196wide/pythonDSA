def firstindexeff(a,x,si):
  if si == len(a):
    return -1
  if a[si] ==x:
    return si
  smallList= firstindexeff(a,x,si+1)
a=[1,2,3,9,5,3,7]
print(firstindexeff(a,1,6))