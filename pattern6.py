cnt=1
for i in range(5,0,-1):
     for j in range(i):
         print("*",end="")

     print()
     for k in range(cnt):
         print("",end=" ")
     cnt+=1   
