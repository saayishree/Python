x=int(input("enter the no"))
for i in range(0,abs(x)+1):
    if i**3>=abs(x):
        break
if i**3!=abs(x):
    print("not a perfect cube")

else:
    if x<0:
        i=-i

    print(i)
           
