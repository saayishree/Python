num=int(input("enter a number:"))
x=0
while abs(num)-x**3:
     x=x+1
if x**3!=abs(num):
  print(num,'is not a perfect cube')
else:
    if x<0:
      x=-x
    print(x,"is the cube root of",num)
    
