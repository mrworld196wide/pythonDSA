def number1ton(n):
  if(n==0):
    return 0
  number1ton(n-1)
  print(n)
  return
  

def numbernto1(n):
  if(n==0):
    return 
  print(n)
  return numbernto1(n-1)
  
n = int(input("enter required no:"))
number1ton(n)
numbernto1(n)
