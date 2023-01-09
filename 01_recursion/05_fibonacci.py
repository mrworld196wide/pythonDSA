def fibo(n):
    if(n==1 or n==2):
      return 1
    out1= fibo(n-1)
    out2= fibo(n-2)
    res = out1 + out2
    return res
n= int(input("enter no:"))
print(fibo(n))