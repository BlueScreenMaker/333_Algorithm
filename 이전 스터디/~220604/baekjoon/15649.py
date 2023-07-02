import itertools
n, m=map(int, input().split())
numList=[]
printList=[]

for i in range(1,n+1):
    numList.append(str(i))

printList=list(map(' '.join, itertools.permutations(numList, m)))
print(printList)
for i in range(0,len(printList)):
    print(printList[i])

