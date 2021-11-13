for n in range(2,10):
    for i in range(2,n):
        if(n%i==0):
            print(n,"is divisible by",i)
            break
    else:
         print(n,"is a prime no")
