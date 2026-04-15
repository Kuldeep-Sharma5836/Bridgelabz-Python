n=int(input("Enter no row : "))
m=int(input("Enter no column :  "))
arr=[]

for i in range(n):
    l=[]
    for i in range(m):
        val=input("Enter the value :")
        l.append(val)
    arr.append(l)
print("The 2D array is : ")

for i in range(n):
    for j in range(m):
        print(arr[i][j],end=" ")
    print()