x=1
large=0
flag=0
while(x<=10):
    num=int(input("enter a no:"))
    if num%2!=0:
        if large<num:
            large=num
    else:flag=flag+1
    x=x+1
if flag==10:
    print("no number is odd")
print("the largest no is",large)    
    
