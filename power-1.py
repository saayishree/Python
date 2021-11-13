num=int(input("enter a number"))
root=0
pwr=0
while 0<pwr<6:
    if root**pwr==num:
        break
    if pwr==6:
        pwr=1
        root=root+1

print(root,pwr)
