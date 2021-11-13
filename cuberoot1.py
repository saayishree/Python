num=int(input("enter a number:"))
ans=0
while ans**3<abs(num):
    ans=ans+1
if ans**3!=abs(num):
    print(num,"is not a perfect cube")
elif num<0:
    ans=-ans
print("cube root of",num,"is",ans)    
