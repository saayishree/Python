# Enter your code here. Read input from STDIN. Print output to STDOUT
T=int(input("Enter the no of test cases:"))

for i in range(T):
    N=int(input("Enter the block size"))
    block=[]

    for j in range(N):
        item=int(input())
        block.append(item)

    k=0
    while(k<N-1 and block[k]>=block[k+1]): //D.O
         k=k+1
    while(k<N-1 and block[k]<=block[k+1]): //A.O     //  D.O OR A.O OR D.O&A.O->YES
                                                     //A.O&D.O->NO
        k=k+1
    if(k==N-1):
        print("Yes")
    else:
        print("No")  
 
