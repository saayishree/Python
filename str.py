n=10
x=int(input("enter a no"))
l=x
while n>=1:
    n=n-1
    if(n==0):
     break
    if x%2!=0 and l<x:
        l=x
    
    x=int(input("enter a no"))


print("the largest is:",l)    
