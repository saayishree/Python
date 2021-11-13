cnt=5
for i in range(1,5):
    print()
    if i==1 or i==3 or i==5:
       for j in range(i):
          for k in range(cnt):
              print(" ",end=" ")
          print(j,end=" ")
          print(" ",end=" ")
    else:
         for l in range(i):
            for q in range(cnt):
                print(" ",end=" ")
            print(l,end=" ")
            print(" ",end=" ")
    cnt-=1        
