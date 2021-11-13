#functions

def copies(s,n):
     tmp=" "
     for i in range(n):
       tmp=tmp+s
     return tmp


print("string:",copies("abc",2))
