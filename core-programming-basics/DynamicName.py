Str="Hello <<UserName>>, How are you?"
name=input("What is your name? ")
if(len(name)<3):
    print("Length is too short")
else:
    str1=Str.replace("<<UserName>>",name)
    print(str1)
