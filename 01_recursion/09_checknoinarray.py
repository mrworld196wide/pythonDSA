def checkno(a,x):
  print(type(a)) 
  print(a)
  l= len(a)
  if(l==0):
    return False
  elif (a[0]==x):
    return True
  else:
    return checkno(a[1:],x)
x= int(input("enter required no:"))
a= [1,2,3,4,5,6,7]
print(checkno(a,x))
    