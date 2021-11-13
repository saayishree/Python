from array import *
a=array('i',[1,2,3,4,5])
for i in range(len(a)):
    print(a[i])
print(a.typecode)
print(a.buffer_info())
b=array(a.typecode,(i for i in a))
print(b)
