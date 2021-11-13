x,y,z=9,3,5
if x%2!=0 and y%2!=0 and z%2!=0:
    if x>y and x>z:
        print('x is larger')
    elif y>x and y>z:
        print('y is larger')
    else:
        print('z is larger')
else:
    print('all are not odd')
