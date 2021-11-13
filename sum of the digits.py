#sum of digits in an integer
x=int(input("enter an integer:"))
k=x
sum=0
while k!=0:
    r=k%10
    sum=sum+r
    k=k//10
print("sum of the digits:",sum)    
