#cube root
num=int(input("enter a number"))
for ans in range(0,abs(num+1)):
    if ans**3>=abs(num):
        break
if ans**3!=abs(num):
    print(num,"is not a perfect cube")
else:
    if(num<0):
        ans=-ans
    print(ans,"is the cube root of ",num)    
