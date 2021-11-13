#cube root
x=int(input("enter a no:"))
ans=0
while ans**3<x:
    ans=ans+1
if ans**3!=x:
    print("x is not a perfect cube")
if x<0:
    ans=-ans
print(ans)    
