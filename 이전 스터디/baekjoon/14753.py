n=int(input())
numList=list(map(int, input().split()))

for a in numList:
    if(a==0):
        numList.remove(a)

numList.sort()

if(len(numList)==0):
    print("0")
elif (len(numList)==1):
    print("0")
elif len(numList)==2:
    if(numList[0]*numList[1]>0):
        print(numList[0]*numList[1])
    else:
        print("0")
elif len(numList)>=3:
    temp=[]
    temp.append(numList[0]*numList[1])
    temp.append(numList[0]*numList[1]*numList[-1])
    temp.append(numList[-1]*numList[-2])
    temp.append(numList[-1]*numList[-2]*numList[-3])
    temp.sort()
    if(temp[-1]>0):
        print(temp[-1])
    else:
        print("0")