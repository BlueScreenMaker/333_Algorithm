import sys
import heapq

N=int(sys.stdin.readline())
heap=[]

for i in range(0,N):
    input_number=int(sys.stdin.readline())
    if input_number!=0:
        heapq.heappush(heap,(-input_number,input_number))
    else:
        if heap:
            print(heapq.heappop(heap)[0])
        else:
            print(0)

'''
def getParent(child):
    return (child-1)//2

def swap(array, c1,c2):
    temp=array[c1]
    array[c1]=array[c2]
    array[c2]=temp

def heapify(array, parentIndex,lastIndex):
    while (parentIndex*2)+1<=lastIndex:
        leftChild=(parentIndex*2)+1
        rightChild=(parentIndex*2)+2
        largeIndex=parentIndex

        if(array[leftChild]>array[largeIndex]):
            largeIndex=leftChild

        if(rightChild<=lastIndex and array[rightChild]>array[largeIndex]):
            largeIndex=rightChild

        if largeIndex!=parentIndex:
            swap(array,parentIndex,largeIndex)
            parentIndex=largeIndex
        else: return


def sort(array, length):
    parentIndex=getParent(length-1)
    for i in range(parentIndex,-1,-1):
        heapify(array,0,length-1)
    print(array[0])
    del array[0]

def checkRoot(array,check):
    parentI=getParent(check)
    while array[check]>array[parentI] and parentI>-1:
        swap(array,check,parentI)
        check=parentI
        parentI=getParent(check)

N=int(sys.stdin.readline())
number=[]
for i in range(N):
    test=int(sys.stdin.readline())
    if test!=0:
        number.append(test)
        checkRoot(number,len(number)-1)
    else:
        if number:
            sort(number, len(number))
        else:
            print(0)
'''




