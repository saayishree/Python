x=int(input("enter an integer"))
pwr=1
root=0
while pwr<6 and pwr>0:
    if root**pwr==x:
        flag=1
        break
    else:
        flag=0
    pwr=pwr+1
    root=root+1
if flag==1:
    print("pwr=",pwr,"root=",root)
elif flag==0:
    print("no such pair of integers")
    
