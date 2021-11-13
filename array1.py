from array import *
a=array('i',[1,2,3,4,5])
print(a)
for i in a:
    print (i)
print(a.typecode)
print(a.buffer_info())
b=array(a.typecode,(i*i for i in a))
print(b)
c=array('u',['a','b','c'])
print(c)
for i in c:
    print(i)
