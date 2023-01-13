def firstindex(a,x):
  if(len(a)==0):
    return -1
  if(a[0]==x):
    return 0
  smallList = a[1:]
  smallout= firstindex(smallList, x)
  if( smallout == -1):
    return -1
  else:
    return smallout+1
a= [1,2,3,4,5,6,7,8,9]
print(firstindex(a,5))