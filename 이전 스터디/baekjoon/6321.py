n=int(input())
stringList=[]
changList=[]
tempString=''
for i in range(0,n):
    stringList.append(input())
for a in range(0,n):
    tempList = list(stringList[a])
    for b in range(0, len(stringList[a])):
        if(ord(tempList[b])==90):
            tempList[b]=65
            tempString += chr(tempList[b])
        else:
            temp=ord(tempList[b])+1
            tempString +=chr(temp)
    changList.append(tempString)
    tempString=''
for i in range(0, len(changList)):
    print("String #",i+1,sep='')
    print(changList[i])
    print()




