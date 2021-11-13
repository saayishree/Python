x,y,z=1,3,5
if x%2!=0 and y%2!=0 and z%2!=0:
    if x>y and x>z:
        print('x is greatest odd')
    elif y>z and y>x:
        print('y is greatesr odd')
    elif z>x:
        print('z is greatest')
else:
    print('all are not odd')
