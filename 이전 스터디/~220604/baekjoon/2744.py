string=input()
stringList=list(string)
change=[]
for i in range(0, len(stringList)):
    if(ord(stringList[i])>=65 and ord(stringList[i])<=90):
        temp=ord(stringList[i])+32
        change.append(chr(temp))
    elif(ord(stringList[i])>=97 and ord(stringList[i])<=122):
        temp=ord(stringList[i])-32
        change.append(chr(temp))

print("".join(map(str, change)))