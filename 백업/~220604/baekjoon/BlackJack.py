from itertools import combinations
n, total=map(int, input().split())
numList=list(map(int, input().split()))
partNumList = []
sumList=[]
for i in range(3,4):
    c=combinations(numList,i)
    partNumList.extend(c)
for i in range(0,len(partNumList)):
    sumList.append(sum(partNumList[i]))
sumList.sort()
for i in range(0, len(sumList)):
    if(sumList[i]>total):
        print(sumList[i-1])
        flag=True
        break
    elif(sumList[i]==total or i==len(sumList)-1):
        print(sumList[i])
        break

