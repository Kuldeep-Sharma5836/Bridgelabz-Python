import random
n=int(input("Enter the times you want to flip the coin: "))
if(n>0):
    head=0
    tail=0
    for i in range(n):
        head=0
        tail=0
        r=random.random()
        if(r<0.5):
            tail=tail+1
        else:
            head=head+1
    print("Head percentage: ",(head/n)*100)
    print("Tail percentage: ",(tail/n)*100)
        
        