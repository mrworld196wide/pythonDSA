'''
def power(x,n):
  if(n==0):
    return 1
  elif(n==1):
    return x
  temp=1
  while(x>0):
    temp= temp*n
    x=x-1
  return temp
x = int(input("enter required no:"))
n = int(input("enter required power:"))
print(power(x,n))
'''
def power(x,n):
  if(n!=0):
    return x * power(x,n-1)
  else:
    return 1
x = int(input("enter required no:"))
n = int(input("enter required power:"))
print(power(x,n))