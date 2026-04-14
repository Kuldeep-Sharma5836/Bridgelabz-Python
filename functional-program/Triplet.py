n=int(input("Enter number of elemnts : "))
arr=[]
for i in range(n):
    v=int(input("Enter : "))
    arr.append(v)
c=0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if(arr[i]+arr[j]+arr[k]==0):
                print(arr[i],arr[j],arr[k])
                c=c+1
print("total triplet",c)
