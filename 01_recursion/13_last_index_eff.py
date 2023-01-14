def lastindex(a,x,si):
  l = len(a)
  if(l==si):
    return -1
  if(a[l-1]==x):
    return l-1
  smallout = lastindex(a[0:l-1], x, si)
  if(smallout == -1):
    return -1
  else:
    return smallout
x= int(input("enter the required no:"))
si= int(input("enter the required index no:"))
a= [1,2,3,4,3,6,3,3,9]
print(lastindex(a,x,si))