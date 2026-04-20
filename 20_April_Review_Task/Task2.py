import json
n=int(input("Enter number students : "))
data={}
for i in range(n):
    name=input("Enter name: ")
    marks=int(input("Enter marks: "))
    data[name]=marks

jsondata=json.dumps(data)
print(jsondata)

for i,j in data.items():
    print('Grade for ',i)
    if(j>=80):
        print('A')
    elif (j >=60 and j<=79):
        print('B')
    elif (j >=50 and j<=69):
        print('C')
    else:
        print('D')