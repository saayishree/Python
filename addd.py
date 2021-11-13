s='1.23,2.4,3.123'
tmp=' '
total=0
for c in s:
    if c!=',':
        tmp=tmp+c
    elif c==',':
        total=total+float(tmp)
        tmp=' '   
total=total+float(tmp)
print(total)
