numList=[]
restList=[]
for i in range(0,10):
    numList.append(int(input()))
for j in range(0,10):
    temp=numList[j]%42
    if(temp in restList):
        continue
    else:
        restList.append(temp)
print(len(restList))