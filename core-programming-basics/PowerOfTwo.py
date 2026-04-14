n=int(input("Enter the number "))
if(n>31):
    print("Number is too large")
else:
    for i in range(n+1):
        print("2^",i,"=",2**i)
