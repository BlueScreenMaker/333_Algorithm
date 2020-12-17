n=int(input())
stringList=[]
total=2015
sumList=[]
for a in range(0,n):
    stringList.append(input())
for i in range(0, len(stringList)):
    tempList=list(stringList[i])
    tempList=list(set(tempList))
    for j in range(0,len(tempList)):
        total=total-ord(tempList[j])
    sumList.append(total)
    total=2015
print("\n".join(map(str, sumList)))