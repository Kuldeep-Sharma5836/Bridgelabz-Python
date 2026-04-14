n=int(input("Enter the number "))
i=2
while(i*i<=n):
    if(n%i==0):
        print(i)
    else:
        i=i+1    
    n=n//i
if(n>1):
    print(n)