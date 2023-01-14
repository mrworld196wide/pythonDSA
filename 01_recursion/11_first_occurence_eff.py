def firstindexeff(a,x,si):
  print (type(a)," : ",a)
  if si == len(a):
    return -1
  if a[si] ==x:
    return si
  smallList= firstindexeff(a,x,si+1)
  return smallList
a=[1,2,3,9,5,6,7,3,3,4,7,9]
print(firstindexeff(a,7,4))