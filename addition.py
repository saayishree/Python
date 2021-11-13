s='1.23,2.4,3.123'
temp=''
num=0
for ch in s:
    if ch!=',':
        temp=temp+ch
    elif ch == ',' :
         num=num+float(temp)
         temp=''
    
num=num+float(temp)
print(num)
