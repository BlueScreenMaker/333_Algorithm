import sys

N=int(sys.stdin.readline())


num=list(map(int, sys.stdin.readline().split()))

num=sorted(num)

ans=0
for i in range(0,N):
    for j in range(0,i+1):
        ans+=num[j]
print(ans)