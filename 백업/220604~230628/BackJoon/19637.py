import sys

N,M=map(int,sys.stdin.readline().split(" "))

stat=[]
for i in range(N):
    string=sys.stdin.readline().split(" ")
    stat.append([string[0],int(string[1])])

power=[]
for j in range(M):
    power.append(int(sys.stdin.readline()))

for z in range(M):
    left=0
    right=N
    mid=(left+right)//2
    while left<=right:
        if power[z]>stat[mid][1]:
            left=mid+1
        else:
            right=mid-1
        mid=(left+right)//2

    print(stat[right+1][0])