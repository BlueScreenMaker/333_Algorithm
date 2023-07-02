import sys

people,M=map(int,sys.stdin.readline().split(" "))

snack=list(map(int,sys.stdin.readline().split(" ")))

left=1
right=max(snack)
answer=0

while left<=right:
    mid=(left+right)//2
    count = 0
    for i in range(M):
        count+=snack[i]//mid
    if count>=people:
        answer=mid
        left=mid+1
    else:
        right=mid-1
print(answer)