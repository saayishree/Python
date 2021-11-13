cnt=1
for i in range(5):
    print()
    for j in range(5):
        if i==0 or i==4: 
          print("S",end=" ")  
        if i==1 or i==2 or i==3:
           if j==0 or j==4:
               print("s",end=" ")
           else: 
               for k in range(3):
                 print(" ",end=" ")   
             
       
    
