x=int(input("enter a no:"))
flag=0
root=1      
      
for pwr in range (6):
      root=0
      while root**pwr<=x:
          root=root+1
        
      if root**pwr==x:
          flag=1
          print("pwr=",pwr,"root=",root)
          break
      
    
if flag==0:
    print("no such pairs exist")
      
      
